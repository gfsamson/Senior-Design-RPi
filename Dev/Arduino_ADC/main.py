#!/usr/bin/env python
# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.dtr = False         # The Arduino makes the pitiful assumption that
                        #       this script is a terminal. This forces it to 
                        #       behave with some damn manners.
time.sleep(2)           # There is also a race condition.
                        #       If you omit this line, it will not work.

try:
    while True:
        time.sleep(0.005)
        ser.write('0')
        ser.write('1')
        X = ser.readline().strip()
        Y = ser.readline().strip()
        print("{0}V {1}V".format(X, Y))
finally:
    ser.close()
