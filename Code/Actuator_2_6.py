## Buzzer

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUZZER = 20

GPIO.setup(BUZZER, GPIO.OUT)

try :
    while True:
        GPIO.output(BUZZER, True)

except KeyboardInterrupt:
    GPIO.cleanup()

