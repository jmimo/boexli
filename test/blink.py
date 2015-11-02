#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

GREEN=7
RED=11

def main():
    prepare()
    state = False 
    gpio = GREEN
    toggle = False
    while True:
        if state:
            off(gpio)
            state = False
            time.sleep(1)
        else:
            on(gpio)
            time.sleep(1)
            state = True
            if toggle:
                toggle = False
                gpio = RED
            else:
                toggle = True
                gpio = GREEN
    GPIO.cleanup()

def prepare():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)

def on_green():
    GPIO.output(7,True)

def off_green():
    GPIO.output(7,False)

def on(gpio):
    GPIO.output(gpio,True)

def off(gpio):
    GPIO.output(gpio,False)

if __name__ == '__main__':
    main()
