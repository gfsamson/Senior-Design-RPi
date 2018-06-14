#!/usr/bin/env python

import sys

# has blink_example()
import main

def q():
    print("Do you want to blink the LED?")
    get_char = sys.stdin.read(1)
    print("You said... {0}".format(get_char))
    if get_char == 'y':
        main.blink_example()
    else:
        print(":(")

if __name__ == "__main__":
    q()
