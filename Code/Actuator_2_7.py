## Servo-Motor

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SERVOMOTOR = 23

GPIO.setup(SERVOMOTOR, GPIO.OUT)
P = GPIO.PWM(SERVOMOTOR, 50)
P.start(0)

try :
    while True:
        P.ChangeDutyCycle(1)
	time.sleep(1)
	P.ChangeDutyCycle(5)
	time.sleep(1)
	P.ChangeDutyCycle(8)
	time.sleep(1)

except KeyboardInterrupt:
    P.stop() 
GPIO.cleanup()

