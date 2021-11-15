import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_PIN = 25

GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
	if GPIO.input(GPIO_PIN) == False:
	    print 'Gas Detected!'
	else :
	    print 'No Gas.'
	time.sleep(1.0)
except KeyboardInterrupt:
    GPIO.cleanup()

