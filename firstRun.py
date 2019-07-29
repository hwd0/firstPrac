#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setwarnings(False)

def call(channel):
	print 'button pressed'
	GPIO.output(3, GPIO.HIGH)
# Logic that you write
def main():
    print("waiting for button press")
	GPIO.add_event_detect(5, GPIO.FALLING, callback=call bouncetime=300)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
			main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)