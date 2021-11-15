## FAN

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

FAN = 6

GPIO.setup(FAN, GPIO.OUT)

try :
    while True:
        GPIO.output(FAN, True)

except KeyboardInterrupt:
    GPIO.cleanup()

