#include "mbed.h"
#include "Servo.h"
#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Bool.h>

//Created by: Steph
//Description: Controls the thrusters, communicates with the Blue Teensy, 
//             and takes in readings from Hydrophones, Batteries, and 
//Microcontroller: Teensy 3.2
//Date: 02/29/2020 


// Thruster code
// Intialize PWM objects (thrusters)

//