#!/usr/bin/env python

import time
import traceback

import RPi.GPIO as GPIO


def sensor_test():
    channel = 37                        # pin index of led (see http://invent.module143.com/wp-content/uploads/2016/06/pi3_gpio-1.png)
    GPIO.setmode(GPIO.BOARD)            # pin indexing method (https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)
    GPIO.setup(channel, GPIO.IN)
    try:
        while True:
            time.sleep(0.01)
            print(GPIO.input(channel))
#            if GPIO.input(channel):
#                print(" - LOW - ")
#            else:
#                print(" - HIGH -")
    except KeyboardInterrupt as kex:    # Detects Ctrl-C.
        print("Stopping! Detected you wanted to cancel..")
    except Exception as ex:
        print("Unknown exception caught! Here are the details:")
        print("------------------------------")
        print("{0}".format(traceback.format_exc()))
        print("------------------------------")
    finally:
        print("Cleaning up..")
        GPIO.cleanup()                  # unsets the "setmode" and "setup" function calls from above.
    

if __name__ == "__main__":
    sensor_test()
