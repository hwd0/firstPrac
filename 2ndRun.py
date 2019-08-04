#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Hamza Waleed
Student Number: WLDHAM001
Prac: 01
Date: <30/07/2019>
"""

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Constants and global variables
count = 0           # used to count number of button presses

btn_add = 35        # selects port 35 for button input
btn_sub = 37        # selects port 37 for button input

led_1 = 40          # selects port 40 for LED output
led_2 = 38          # selects port 38 for LED output
led_3 = 36          # selects port 36 for LED output

# Setup ports for input and output
GPIO.setup(btn_add, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 35 to be an input pin and set initial value to be pulled high
GPIO.setup(btn_sub, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 37 to be an input pin and set initial value to be pulled high

GPIO.setup(led_1, GPIO.OUT)                    # Set pin 40 to be an output
GPIO.setup(led_2, GPIO.OUT)                    # Set pin 38 to be an output
GPIO.setup(led_3, GPIO.OUT)                    # Set pin 36 to be an output


def add(channel):  # callback function when 'add button' is pressed
    global count
    print("Button_ADD was pushed!")
    count = count +1
    print("Counter = "+str(count)+".\n")
    bin_display()  # displays to LEDs

def sub(channel):  # callback function when 'subtract button' is pressed
    global count
    print("Button_SUBTRACT was pushed!")
    count = count -1
    print("Counter = "+str(count)+".\n")
    bin_display()  # displays to LEDs
    
def bin_display():  # function displays binary on three LEDs
    global led_1
    global led_2
    global led_3
    
    bin_dis = count%8
    
    if bin_dis==0:
        GPIO.output(led_1,0)
        GPIO.output(led_2,0)
        GPIO.output(led_3,0)
    elif bin_dis==1:
        GPIO.output(led_1,1)
        GPIO.output(led_2,0)
        GPIO.output(led_3,0)
    elif bin_dis==2:
        GPIO.output(led_1,0)
        GPIO.output(led_2,1)
        GPIO.output(led_3,0)
    elif bin_dis==3:
        GPIO.output(led_1,1)
        GPIO.output(led_2,1)
        GPIO.output(led_3,0)
    elif bin_dis==4:
        GPIO.output(led_1,0)
        GPIO.output(led_2,0)
        GPIO.output(led_3,1)
    elif bin_dis==5:
        GPIO.output(led_1,1)
        GPIO.output(led_2,0)
        GPIO.output(led_3,1)
    elif bin_dis==6:
        GPIO.output(led_1,0)
        GPIO.output(led_2,1)
        GPIO.output(led_3,1)
    elif bin_dis==7:
        GPIO.output(led_1,1)
        GPIO.output(led_2,1)
        GPIO.output(led_3,1)
    else:
        GPIO.output(led_1,0)
        GPIO.output(led_2,0)
        GPIO.output(led_3,0)
       
# Detect button press using interuppts
GPIO.add_event_detect(btn_add,GPIO.FALLING,callback=add, bouncetime=300) # Setup event on pin 35 falling edge
GPIO.add_event_detect(btn_sub,GPIO.FALLING,callback=sub, bouncetime=300) # Setup event on pin 37 falling edge

bin_display() # display binary output
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up