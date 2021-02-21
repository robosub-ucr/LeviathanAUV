#define UART Serial1

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//STRUCT DEFINITIONS

//Thruster struct
typedef struct Thruster {
  unsigned char duty_cycle = 128; //baseline = off; 0 = full power backwards; 255 = full power forwards
  unsigned char pin;
}thruster;

//Task struct
typedef struct Tasks {
  int state = 0;
  unsigned long period = 0;
  unsigned long elapsed_time = 0;
  int (*TickFct)(int);
  bool Active = true;
} task;
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//GLOBAL VARIABLES

int global_period = 25000;

unsigned int UART_reader;

//IntervalTimer is a Teensy specific clock cycle based system that allows for an interrupt driven system of State machines
//further details found on teensy's webpage
IntervalTimer myTimer;

//baseline is a TESTCASE PIN used to test baseline values
thruster BASELINE;
char BASELINE_PIN = 9;
char BASELINE_VAL = 125;

//thruster_Array is an array of pins that will send PWM signals to ESCs
thruster Thruster_Array[8];
int Pin_Array[8] = {3,4,5,6,20,21,22,23}; 

const unsigned char  tasks_size = 2;
task Tasks[tasks_size];

/* 
THRUSTER ARRAY MAP

    front
(0) ____ (7)
   |    |
(1)|    |(6)
(2)|    |(5)
   |____|
(3)      (4)
    back
    
*number 0-7 correspond to position in array

  unsigned 64bit int          [8][8][8][8][8][8][8][8] < 64bit int
  partitioned such that       [7][6][5][4][3][2][1][0] < thruster array
  
  */
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void setup() {
  pinMode(13, OUTPUT); //for above test-LED
  
  //set up UART communication
  UART.begin(58824);
  
  //init pin_array as output, BASELINE_PIN output, A9 input
  unsigned char i = 0;
  for(i = 0; i < 8; i++) {
    pinMode(Pin_Array[i],OUTPUT);
  }
    pinMode(BASELINE_PIN, OUTPUT);
    

  //init thruster array with pin values
  for (i = 0; i < 8; i++) {
    Thruster_Array[i].pin = Pin_Array[i];
  }
  //init BASELINE values
  BASELINE.pin = BASELINE_PIN;
  BASELINE.duty_cycle = BASELINE_VAL;
  
  //initialize tasks tasks

  //PollUART
  //desc: every global_period, will update the intended values of PWMs
  Tasks[0].state = 0;
  Tasks[0].period = global_period;
  Tasks[0].elapsed_time = 0;
  Tasks[0].TickFct = &PollUART; //this function reads from the other MC through UART, updating duty cycles
  Tasks[0].Active = true;//always happening, but run once on startup

  //OutputPWM (triggered SM)
  Tasks[1].state = 0;
  Tasks[1].period = 0;
  Tasks[1].elapsed_time = 0;
  Tasks[1].TickFct = &OutputPWM;
  Tasks[1].Active = true;//will need to be triggered, but run once on startup
  //this is a triggered SM to not take up proccessing power when thruster states are not changed

  //STALL WHILE UART NOT ESTABLISHED
  /*while(!(UART.available() > 0)) {
    digitalWrite(13,HIGH);
    delay(700);
    digitalWrite(13,LOW);
    delay(100);
    UART_reader = UART.read();
  }*/
  digitalWrite(13,LOW);
  
  //begin timer at the end of setup
  //will interrupt process to run "Scheduler" function every global_period (microseconds (not sure, but it's fast))
  myTimer.begin(Scheduler, global_period); //begin scheduler
  
}
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//runs every global_period
//just a scheduler
void Scheduler(){
  unsigned char i;
  for (i = 0; i < tasks_size; i++){
    if (Tasks[i].Active) {
      if (Tasks[i].elapsed_time >= Tasks[i].period) {
        Tasks[i].state = Tasks[i].TickFct(Tasks[i].state);
        Tasks[i].elapsed_time = 0;        
      }
      Tasks[i].elapsed_time += global_period;
    }
  }
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//updates PWMs
//Triggered SM, trigger is in TSubCB()
int OutputPWM(int state) {
 unsigned char i;
  for (i = 0; i < 8; i++) {
   analogWrite(Thruster_Array[i].pin, Thruster_Array[i].duty_cycle);
  }
  
  //update BASELINE pwm (but like... when would you want to?)
  analogWrite(BASELINE.pin, BASELINE.duty_cycle);
  Tasks[1].Active = false;//turn itself off as to not run again
  
  return 0; 
  
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//poll UART

int PollUART(int state){
  unsigned char i = UART.available() > 16 ? 16: UART.available();
  unsigned char t; // which thruster to write to
  unsigned char s; // whether its MSB or LSB
  unsigned char d; // actual data
  for (unsigned char y = 0; y < i; y++){
    UART_reader = UART.read(); //read from UART
    t = UART_reader >> 5;
    s = (UART_reader >> 4) % 2; //0 = MSB , 1 = LSB
    d = UART_reader % 16;
    Thruster_Array[t].duty_cycle = (s == 0)? (Thruster_Array[t].duty_cycle & 0b00001111)+(d*16) : (Thruster_Array[t].duty_cycle & 0b11110000)+d; 
  }
  if (i > 0){
    digitalWrite(13,!digitalRead(13));
    Tasks[1].Active = true;} //update PWMs next clockcyclebv

  return 0;
  
}

//nothing needs to happen in loop because it'll be interuppted by intervalTimer
//ideally would put to sleep or some low power mode
void loop() {}
