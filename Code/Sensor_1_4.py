# Pyroelectric ("Passive") InfraRed Sensor

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_PIN = 27

GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(GPIO_PIN) == True:
            print 'Detected.'
        else :
            print 'Not detected.'
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()


