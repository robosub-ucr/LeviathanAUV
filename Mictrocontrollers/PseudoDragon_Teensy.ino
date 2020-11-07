//ROS Library
#include <ros.h>
//Unsigned 64-bit int ROS-node type
#include <std_msgs/UInt64.h>

//this just needs to be declared before anything else, because reasons
ros::NodeHandle nh;

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

  UInt64 (unsigned 64bit int) [8][8][8][8][8][8][8][8] < 64bit int
  partitioned such that       [7][6][5][4][3][2][1][0] < thruster array
  
  */
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//ROS stuff

//init ros 8bit int array variable
std_msgs::UInt64 arr_msg;

//runs after PollSubscribers, which causes the subscriber to spinonce()
//(spinonce() is what causes this function to be called)
//bitmasks arr_msg 
//each pin's PWM can be changed separately
void TSubCB(const std_msgs::UInt64& arr_msg) {
  unsigned char i;
  unsigned long long temp = arr_msg.data;
  for (i = 0; i < 8; i++) {
    temp = arr_msg.data;
    Thruster_Array[i].duty_cycle = ( (temp >> (8*i)) &0xFF );
  }
  Tasks[1].Active = true;
  digitalWrite(13,HIGH-digitalRead(13)); //just a test for whether callback is being called 
}

//init ROS subscriber to subscribe to node "ThrusterStates" and run TSubCB after it polls
ros::Subscriber<std_msgs::UInt64> TSub("ThrusterStates", &TSubCB); //"ThrusterStates is name of ROS topic

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void setup() {
  pinMode(13, OUTPUT); //for above test-LED
  
  nh.initNode();//init ROS node
  nh.subscribe(TSub); //init subcription
  
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

  //PollSubscribers
  //desc: every global_period, will run spinonce(), updating everything ROS related (sending publishing topics, reading subscribing topics)
  Tasks[0].state = 0;
  Tasks[0].period = global_period;
  Tasks[0].elapsed_time = 0;
  Tasks[0].TickFct = &PollSubscribers; //this function runs SpinOnce(), which will update the teensy on what its subscriber is publishing
  Tasks[0].Active = true;//always happening, but run once on startup

  //OutputPWM (triggered SM)
  Tasks[1].state = 0;
  Tasks[1].period = 0;
  Tasks[1].elapsed_time = 0;
  Tasks[1].TickFct = &OutputPWM;
  Tasks[1].Active = true;//will need to be triggered, but run once on startup
  //this is a triggered SM to not take up proccessing power when thruster states are not changed
  
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
//poll ROS subcribers
int PollSubscribers(int state){
  nh.spinOnce();
  return 0;
  
}
//nothing needs to happen in loop because it'll be interuppted by intervalTimer
//ideally would put to sleep or some low power mode
void loop() {}
