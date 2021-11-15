## Ultrwave Sensor
## HC-SRO4

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGGER = 18
ECHO = 21

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
	GPIO.output(TRIGGER, False)
	time.sleep(0.5)

	GPIO.output(TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)

	while GPIO.input(ECHO) == 0:
	    pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
	    pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17000
	distance = round(distance, 2)

	print 'distance: ', distance, 'cm'
	time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
