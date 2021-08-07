#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

Left = 11    # define Left turn
Right = 13    # define Right turn
Forward = 31    # define Forward movement
Rear = 29    # define Rear movement

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(Left, GPIO.OUT)   # set the Left to OUTPUT mode
    GPIO.output(Left, GPIO.LOW)  # make Left output LOW level
    print ('using pin%d'%Left)

    GPIO.setup(Right, GPIO.OUT)   # set the Right to OUTPUT mode
    GPIO.output(Right, GPIO.LOW)  # make Right output LOW level
    print ('using pin%d'%Right)

    GPIO.setup(Forward, GPIO.OUT)   # set the Forward to OUTPUT mode
    GPIO.output(Forward, GPIO.LOW)  # make Forward output LOW level
    print ('using pin%d'%Forward)

    GPIO.setup(Rear, GPIO.OUT)   # set the Rear to OUTPUT mode
    GPIO.output(Rear, GPIO.LOW)  # make Rear output LOW level
    print ('using pin%d'%Rear)

def loop():
    while True:
        GPIO.output(Left, GPIO.HIGH)  # make Left output HIGH level to turn the car left
        print ('Left turned on >>>')     # print information on terminal
        time.sleep(5)                   # Wait for 5 second
        GPIO.output(Left, GPIO.LOW)   # make Left output LOW level to turn off left turn
        print ('Left turned off <<<')
        time.sleep(1)                   # Wait for 1 second

        GPIO.output(Right, GPIO.HIGH)  # make Right output HIGH level to turn the car left
        print ('Right turned on >>>')     # print information on terminal
        time.sleep(5)                   # Wait for 5 second
        GPIO.output(Right, GPIO.LOW)   # make Right output LOW level to turn off right turn
        print ('Right turned off <<<')
        time.sleep(1)                   # Wait for 1 second

        GPIO.output(Forward, GPIO.HIGH)  # make Forward output HIGH level to move the car Forward
        print ('Forward turned on >>>')     # print information on terminal
        time.sleep(5)                   # Wait for 5 second
        GPIO.output(Forward, GPIO.LOW)   # make Forward output LOW level to turn off Forward movement
        print ('Forward turned off <<<')
        time.sleep(1)                   # Wait for 1 second

        GPIO.output(Rear, GPIO.HIGH)  # make Rear output HIGH level to move the car Rear
        print ('Rear turned on >>>')     # print information on terminal
        time.sleep(5)                   # Wait for 5 second
        GPIO.output(Rear, GPIO.LOW)   # make Rear output LOW level to turn off Rear movement
        print ('Rear turned off <<<')
        time.sleep(5)                   # Wait for 1 second

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()