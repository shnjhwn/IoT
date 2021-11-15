
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_PIN = 22

GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(GPIO_PIN) == False:
            print 'Near Proximity Sensor'
        else :
            print 'Far from Proximity Sensor'
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()


