import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)



GPIO.cleanup()