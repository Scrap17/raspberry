########################################################################
# Filename    : kbtest.py
# Description : keyboard usage test.
# author      : David Garcia-Taheño Fernandez
# modification: 23/10/2021
########################################################################
import RPi.GPIO as GPIO
import sys, tty, termios, time

# GPIO initialization
Left = 11    # define Left turn
Right = 13    # define Right turn
Forward = 31    # define Forward movement
Rear = 29    # define Rear movement

def setup():
    GPIO.setmode(GPIO.BOARD)    # use PHYSICAL GPIO Numbering

    GPIO.setup(Left, GPIO.OUT)    # set the Left to OUTPUT mode
    GPIO.output(Left, GPIO.LOW)    # make Left output LOW level
    print ('using pin%d for Left'%Left)

    GPIO.setup(Right, GPIO.OUT)    # set the Right to OUTPUT mode
    GPIO.output(Right, GPIO.LOW)    # make Right output LOW level
    print ('using pin%d for Right'%Right)

    GPIO.setup(Forward, GPIO.OUT)    # set the Forward to OUTPUT mode
    GPIO.output(Forward, GPIO.LOW)    # make Left output LOW level
    print ('using pin%d for Forward'%Left)

    GPIO.setup(Rear, GPIO.OUT)    # set the Rear to OUTPUT mode
    GPIO.output(Rear, GPIO.LOW)    # make Rear output LOW level
    print ('using pin%d for Rear'%Rear)

# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# This section of code defines the methods used to determine
# whether a motor needs to spin forward or backwards. The
# different directions are acheived by setting one of the
# GPIO pins to true and the other to false. If the status of
# both pins match, the motor will not turn.
def forward():
    GPIO.output(Forward, GPIO.HIGH)
    print ('Forward turned on >>>')
    delay()

def rear():
    GPIO.output(Rear, GPIO.HIGH)
    print('Rear turned on >>>')
    delay()

def left():
    GPIO.output(Left, GPIO.HIGH)
    print ('Left turned on >>>')
    delay()

def right():
    GPIO.output(Right, GPIO.HIGH)
    print ('Right turned on >>>')
    delay()

# This method will toggle the lights on/off when the user
# presses a particular key. It will then change the status
# of the lights so it will know whether to turn them on or
# off when it is next called.
# def toggleLights():

  #  global lightStatus

  #  if(lightStatus == False):
   #     io.output(18, True)
    #    io.output(23, True)
     #   lightStatus = True
   # else:
    #    io.output(18, False)
     #   io.output(23, False)
      #  lightStatus = False

def delay():
    time.sleep(1)

# Instructions for when the user has an interface
if __name__ =='__main__':
    print('Program is starting ...\n')
    setup()
    print("w/s: acceleration")
    print("a/d: steering")
    print("l: lights")
    print("x: exit")

    # Infinite loop that will not end until the user presses the
    # exit key
    while True:
        # Keyboard character retrieval method is called and saved
        # into variable
        char = getch()

        # The car will drive forward when the "w" key is pressed
        if(char == "w"):
            forward()

        # The car will reverse when the "s" key is pressed
        if(char == "s"):
            rear()

        # The "a" key will toggle the steering left
        if(char == "a"):
            left()

        # The "d" key will toggle the steering right
        if(char == "d"):
            right()

        # The "l" key will toggle the LEDs on/off
        #if(char == "l"):
         #   toggleLights()

        # The "x" key will break the loop and exit the program
        if(char == "x"):
            print("Program Ended")
            break

        # At the end of each loop the acceleration motor will stop
        # and wait for its next command
        GPIO.output(Left, GPIO.LOW)
        GPIO.output(Right, GPIO.LOW)
        GPIO.output(Forward, GPIO.LOW)
        GPIO.output(Rear, GPIO.LOW)

        # The keyboard character variable will be set to blank, ready
        # to save the next key that is pressed
        char = ""

    # Program will cease all GPIO activity before terminating
    GPIO.cleanup()
