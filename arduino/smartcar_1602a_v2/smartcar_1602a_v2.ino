
/* 
 * Project : Smart Car Project
 * Device  : Arduino + Shield V5 + L298N + Ultrasonic sencer + SG90 survo motor 
 * Athor   : Yoshi Sakai 
 * Project start : 14-Oct-2016
*/
#include <Servo.h> 
#include <NewPing.h>
#include <Wire.h>

#define MAX_DISTANCE 200
#define TRIG_PIN A0
#define ECHO_PIN A1
#define LEFT_PWM A2 // Speed controll
#define LEFT_FORWARD 2
#define LEFT_BACKWARD 3
#define RIGHT_FORWARD 4
#define RIGHT_BACKWARD 5

#define RIGHT_PWM A3 // Speed controll
#define CLEANNER_ON 8 // Cleanner Switch
#define UNDER_TRIG_PIN 12
#define UNDER_ECHO_PIN 13

// For I2C wire
int SLAVE_ADDRESS = 0x04;
int wire_cmd = 0;
int wire_val = 0;

// create Sonor
NewPing sonar = NewPing(TRIG_PIN, ECHO_PIN, MAX_DISTANCE); 
NewPing sonar_under = NewPing(UNDER_TRIG_PIN, UNDER_ECHO_PIN, MAX_DISTANCE); 
int under_dist = 0;
int max_dist = 0;
int max_dist_dig = 90;
int min_dist = 200;
int min_dist_dig = 90;
int distance = 0;
int centerDistance = 200;
int leftDistance = 0;
int rightDistance = 0;

// create servo object to control a servo 
Servo myServo;  
char dist[3];
char rot[3];
int adjust = 0;
String output = "";
int search_wait = 250;
int see_left_dig = 120;
int see_right_dig = 60;
int see_left_dig_wide = 135;
int see_right_dig_wide = 45;
/**
 * Set up LED and Sonor and Servo
 */
void setup() {
  // for motor
  pinMode(LEFT_FORWARD, OUTPUT);
  pinMode(RIGHT_FORWARD, OUTPUT);
  pinMode (TRIG_PIN, OUTPUT);
  pinMode (ECHO_PIN, INPUT);
  myServo.attach(10);  // attaches the servo on pin 0 to the servo object 

  // for NewPing
  distance = sonar.ping_cm();
  Serial.println(distance);

  // for I2C wire
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveAnalogReading);
  Wire.onRequest(sendData);
  Serial.begin(9600);

  Serial.println("Ready!");
  delay(1000);  // Wait 1 Sec
  myServo.write(90);
}

int getSonar() {
  under_dist = sonar_under.ping_cm();
  while(1){
    distance = sonar.ping_cm();
    if (distance != 0){
      break;
    }
    delay(1);
  }
  debugDist(distance);
  return distance;
}

void turnRight(int wait){
  digitalWrite(LEFT_FORWARD,LOW);
  digitalWrite(RIGHT_FORWARD,HIGH);
  digitalWrite(LEFT_BACKWARD,HIGH);
  digitalWrite(RIGHT_BACKWARD,LOW);
  delay(wait);
  stopMotor();
}

void turnLeft(int wait){
  digitalWrite(LEFT_FORWARD,HIGH);
  digitalWrite(RIGHT_FORWARD,LOW);
  digitalWrite(LEFT_BACKWARD,LOW);
  digitalWrite(RIGHT_BACKWARD,HIGH);
  delay(wait);
  stopMotor();
}
/*  Move forward function
 *  Spd (Int) { 0 <-> 255 }
 */
void goOn(){
  digitalWrite(LEFT_FORWARD,HIGH);
  digitalWrite(RIGHT_FORWARD,HIGH);
  digitalWrite(LEFT_BACKWARD,LOW);
  digitalWrite(RIGHT_BACKWARD,LOW);
  digitalWrite(CLEANNER_ON,HIGH);
}
void stopMotor(){
  digitalWrite(LEFT_FORWARD,LOW);
  digitalWrite(RIGHT_FORWARD,LOW);
  digitalWrite(LEFT_BACKWARD,LOW);
  digitalWrite(RIGHT_BACKWARD,LOW);
}

void debugDist(int d){
  sprintf(dist,"%3d",d);
  Serial.print("Range:");
  Serial.print(dist);
  Serial.print("cm");
}
void debugDig(int d){
  sprintf(rot,"%3d",d);
  Serial.print(rot);
  Serial.println("deg");
}

void moveBackward(int d,int deg, int spd){
  Serial.println("Take Back:");
  digitalWrite(LEFT_FORWARD,LOW);
  digitalWrite(RIGHT_FORWARD,LOW);
  digitalWrite(LEFT_BACKWARD,HIGH);
  digitalWrite(RIGHT_BACKWARD,HIGH);
  // Set motor speed to spd
  analogWrite(LEFT_PWM, spd);
  analogWrite(RIGHT_PWM, spd);
  while(1){
    myServo.write(deg);  
    delay(200);
    distance = getSonar();
    debugDist(distance);
    if (distance > d){
      break;
    }
  }
  stopMotor();
}

/**
 * Set min and Max degree and distance
 */
void setMinAndMax(int deg, int distance){
    debugDist(distance);
    debugDig(deg);
    if (max_dist < distance){
      max_dist = distance;
      max_dist_dig = deg;
    }
    if (min_dist > distance){
      min_dist = distance;
      min_dist_dig = deg;
    }  
}
/*
 * maxDeg 10 to 80
 */
void searchRight(int maxDeg){
  int til = 0;
  // scan center to left
  for (int deg = maxDeg; deg < 90; deg+=5) {
    myServo.write(deg);
    delay(search_wait);
    distance = getSonar();
    setMinAndMax(deg, distance);
  }
}
/*
 * 170 to 100
 */
void searchLeft(int maxDeg){
  int til = 0;
  // scan center to right
  for (int deg = maxDeg; deg > 90; deg-=5) {
    myServo.write(deg);
    delay(search_wait);
    distance = getSonar(); 
    setMinAndMax(deg, distance);
  }
}
/*
 * Search Center
 */
void searchCenter(){
  myServo.write(90);
  delay(search_wait);
  distance = getSonar(); 
  Serial.print("search Center");  
  setMinAndMax(90, distance); 
}

void do_command(){
  if (wire_val==255){
    stopMotor();
    debugDist(distance);
  }else if (wire_val==254){
    Serial.println("Cleaner ON");
    digitalWrite(CLEANNER_ON,HIGH);
  }else if (wire_val==253){
    Serial.println("Cleaner OFF");
    digitalWrite(CLEANNER_ON,LOW);
  }else if (wire_val==4){
    Serial.println("DC 4 to 6 o'clock");
    turnLeft(200);
  }else if (wire_val==5){
    Serial.println("DC 5 to 6 o'clock");
    turnLeft(100);
  }else if (wire_val==6){
    Serial.println("Go Stright!");
    goOn();
  }else if (wire_val==7){
    Serial.println("DC 7 to 6 o'clock");
    turnRight(100);
  }else if (wire_val==8){
    Serial.println("DC 8 to 6 o'clock");
    turnRight(200);
  }else if (wire_val==9){
    Serial.println("Survo to 9 o'clock");
    digitalWrite(CLEANNER_ON,LOW);
    myServo.write(0 + adjust);
  }else if (wire_val==10){
    myServo.write(30 + adjust);
  }else if (wire_val==11){
    myServo.write(60 + adjust);
  }else if (wire_val==12){
    digitalWrite(CLEANNER_ON,HIGH);
    myServo.write(90 + adjust);
  }else if (wire_val==13){
    myServo.write(120 + adjust);  
  }else if (wire_val==14){
    myServo.write(150 + adjust);  
  }else if (wire_val==15){
    Serial.println("Survo to 15 o'clock");
    digitalWrite(CLEANNER_ON,LOW);
    myServo.write(180 + adjust);  
  } 
}
/**
 * Main loop
 */
void loop() {
    distance = sonar.ping_cm();
    if (distance>0 && distance<5){
        stopMotor();
    }
}
/**
 * マスタからデータが送られてきたときに呼ばれる
 */
void receiveAnalogReading(){
  int byteCount = 1;
  Serial.println("recept data: ");
  while(Wire.available()) {
    wire_val = Wire.read();
    Serial.print(wire_val);
    do_command();
    Serial.print(" ");
    wire_val = 0; 
  }
  Serial.println();
}
/**
 * マスタからデータのリクエストが来たときに呼ばれる
 */
void sendData(){
  Wire.write(distance);
}
