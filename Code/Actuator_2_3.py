## DC Motor
## PWM 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

DC_MOTOR = 13
GPIO.setup(DC_MOTOR, GPIO.OUT)

P = GPIO.PWM(DC_MOTOR, 100)
P.start(0)

try :
    while True:
	GPIO.output(DC_MOTOR, True)
	for x in range(100):
	    P.ChangeDutyCycle(x)
	    time.sleep(0.1)

	for x in range(100, 0, -1):
	    P.ChangeDutyCycle(x)
	    time.sleep(0.5)

	GPIO.output(DC_MOTOR, False)
	for x in range(100):
            P.ChangeDutyCycle(x)
            time.sleep(0.1)

        for x in range(100, 0, -1):
            P.ChangeDutyCycle(x)
            time.sleep(0.5)

        # GPIO.output(DC_Motor, True)

except KeyboardInterrupt:
    GPIO.cleanup()

