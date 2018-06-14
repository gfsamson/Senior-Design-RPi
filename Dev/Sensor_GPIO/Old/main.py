#!/usr/bin/env python

import time
import traceback

import RPi.GPIO as GPIO


def blink_example():
    channel = 40                        # pin index of led (see http://invent.module143.com/wp-content/uploads/2016/06/pi3_gpio-1.png)
    GPIO.setmode(GPIO.BOARD)            # pin indexing method (https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)
    GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
    try:
        while True:
            time.sleep(1)
            GPIO.output(channel, 1)
            time.sleep(1)
            GPIO.output(channel, 0)
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
    blink_example()
