import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)

while True:
	GPIO.output(3, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.5)


GPIO.cleanup()