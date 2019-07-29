#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Hamza
Student Number: wldham001
Prac: 01
Date: <29/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setwarnings(False)

# Logic that you write
def main():
    print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        GPIO.wait_for_edge(5, GPIO.FALLING)
		GPIO.output(3, HIGH)
	
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
