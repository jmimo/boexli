#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

def main():
    prepare()
    state = False 
    while True:
        if state:
            off()
            state = False
            time.sleep(1)
        else:
            on()
            time.sleep(1)
            state = True
    GPIO.cleanup()

def prepare():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

def on():
    GPIO.output(7,True)

def off():
    GPIO.output(7,False)


if __name__ == '__main__':
    main()
