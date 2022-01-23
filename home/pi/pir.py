#!/usr/bin/python

import sys
import time
import RPi.GPIO as io 
import subprocess

io.setmode(io.BOARD)
DARK_DELAY = 180 #this is where you define after how many seconds you want the display to go dark when there is no motion detected
PIR_PIN=11 #if you connect to another pin, specify here

def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
    while True:
        if io.input(PIR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + DARK_DELAY):
                turned_off = True
                turn_off()
            if not turned_off and time.time() > (last_motion_time + 1):
                time.sleep(.1)
def turn_on():
    CONTROL = "vcgencmd"
    CONTROL_UNBLANK = [CONTROL, "display_power", "1"]
    subprocess.call(CONTROL_UNBLANK)

def turn_off():
    CONTROL = "vcgencmd"
    CONTROL_BLANK = [CONTROL, "display_power", "0"]
    subprocess.call(CONTROL_BLANK)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
