## Flame Sensor

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_PIN = 24

GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(GPIO_PIN) == False:
            print 'Flame detected.'
        else :
            print 'There is no Flame.'
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
                     
