## RGB LED
## PWM

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RGB = 19
GPIO.setup(RGB, GPIO.OUT)

P = GPIO.PWM(RGB, 100)
P.start(0)

try :
    while True:
        # GPIO.output(RGB, True)

	for x in range(100):
	    P.ChangeDutyCycle(x)
	    time.sleep(0.01)

	for x in range(100, 0, -1):
            P.ChangeDutyCycle(x)
            time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()

