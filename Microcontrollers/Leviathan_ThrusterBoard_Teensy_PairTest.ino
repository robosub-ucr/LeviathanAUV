#define UART Serial1

int i;

void setup() {
  i = 0;
  
  Serial.begin(9600);
  UART.begin(9600);

  UART.setRX(0);
  UART.setTX(0);

  //STALL WHILE UART NOT ESTABLISHED
  while(!UART.available()) {
    digitalWrite(13,HIGH);
    delay(700);
    digitalWrite(13,LOW);
    delay(100);
  }
  digitalWrite(13,LOW);
}

void updatePWM() {
  UART.flush(); //flush stream from overflowing
  UART.write(255*pow(2,i));
  i = i <= 8 ? i++: 1;
}

void loop() {
  updatePWM();
  delay(750);
}
