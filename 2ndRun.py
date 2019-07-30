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

count = 0

def add(channel):
    global count
    print("Button_ADD was pushed!")
    count = count +1
    print("Counter = "+str(count)+".\n")
    bin_display()

def sub(channel):
    global count
    print("Button_SUBTRACT was pushed!")
    if count >0:
        count = count -1
    else:
        count = count
    print("Counter = "+str(count)+".\n")
    bin_display()
    
def bin_display():
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
       
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering


btn_add = 35
btn_sub = 37

GPIO.setup(btn_add, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(btn_sub, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_1 = 40
led_2 = 38
led_3 = 36

GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)

GPIO.add_event_detect(btn_add,GPIO.FALLING,callback=add, bouncetime=300) # Setup event on pin 10 rising edge
GPIO.add_event_detect(btn_sub,GPIO.FALLING,callback=sub, bouncetime=300)
bin_display() 
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up