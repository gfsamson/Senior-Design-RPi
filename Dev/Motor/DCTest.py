#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import RPi.GPIO as GPIO

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
motor1 = mh.getMotor(2)
#motor2 = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
motor1.setSpeed(75)
#motor2.setSpeed(0)
try:
    motor1.run(Adafruit_MotorHAT.FORWARD);
    motor1.setSpeed(75);
    time.sleep(100)
finally:
# turn on motor
    motor1.run(Adafruit_MotorHAT.RELEASE);


#while (True):
#	print "Forward! "
# 	motor1.run(Adafruit_MotorHAT.FORWARD)
# 
# 	print "\tSpeed up..."
# 	for i in range(max_speed):
# 		motor1.setSpeed(i)
# 		time.sleep()
# 
# 	print "\tSlow down..."
# 	for i in reversed(range(max_speed)):
# 		motor1.setSpeed(i)
# 		time.sleep(0.01)
#
# 	print "Backward! "
# 	motor1.run(Adafruit_MotorHAT.BACKWARD)
#
# 	print "\tSpeed up..."
# 	for i in range(max_speed):
# 		motor1.setSpeed(i)
# 		time.sleep(0.01)
# 
# 	print "\tSlow down..."
# 	for i in reversed(range(max_speed)):
# 		motor1.setSpeed(i)
# 		time.sleep(0.01)
# 
# 	print "Release"
# 	motor1.run(Adafruit_MotorHAT.RELEASE)
# 	time.sleep(1.0)
