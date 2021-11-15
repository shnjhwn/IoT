## Water Pump

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

WATERPUMP = 5

GPIO.setup(WATERPUMP, GPIO.OUT)

try :
    while True:
	GPIO.output(WATERPUMP, True)

except KeyboardInterrupt:
    GPIO.cleanup()
