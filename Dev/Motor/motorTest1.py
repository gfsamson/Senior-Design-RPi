#!/user/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit

half = 510
home = 0


mh = Adafruit_MotorHAT(addr = 0x60)
def turnoOffMotor():
    mh.getMotor().run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor().run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor().run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor().run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

motor1 = mh.getMotor(3)
motor1.setSpeed(100)
motor2 = mh.getMotor(4)
motor2.setSpeed(100)
myStepper = mh.getStepper(200, 1)
myStepper.setSpeed(60)

def runDC():
    print("DC motors spinning")
    if (position = home)
        try:
        while (sensor_signal != TRUE)
            motor1.run(Adafruit_MotorHAT.FORWARD)
    elif (position = half)
        try:
        while (sensor_signal != TRUE)
            motor2.run(Adafruit_MotorHAT.FORWARD)

def runStepper():
    print("Single Stepping like a boss")
    myStepper.step(1020, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
    position = position + 1020
    position = position % 1020
# myStepper.step(1020, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

def halfRotStepper():
    print("Only Halfway this time")
    myStepper.step(510, Adafruit_MotorHAt.FORWARD, Adafruit_MotorHAT.DOUBLE)
    position = position + 510
    position = position % 1020
runStepper()
