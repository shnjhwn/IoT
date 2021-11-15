## LED BAR
## PWM
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_Bar = 12

GPIO.setup(LED_Bar, GPIO.OUT)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

P_R = GPIO.PWM(4, 2000)
P_B = GPIO.PWM(2, 2000)
P_G = GPIO.PWM(3, 2000)

P_R.start(0)
P_G.start(0)
P_B.start(0)

def SetColor(R, G, B):
    P_R.ChangeDutyCycle(R)
    P_G.ChangeDutyCycle(G)
    P_B.ChangeDutyCycle(B)
    time.sleep(0.001)

def Turnoff():
    P_R.ChangeDutyCycle(0)
    P_G.ChangeDutyCycle(0)
    P_B.ChangeDutyCycle(0)
    time.sleep(0.01)

try :
    while True:
        # GPIO.output(LED_Bar, True)
	for x in range(99):
	    SetColor(100 - x, x, 0)

	for x in range(99):
            SetColor(0, 100 - x, x)

	for x in range(99):
            SetColor(x, 0, 100 - x)

except KeyboardInterrupt:
    GPIO.cleanup()
    P_R.stop()
    P_G.stop()
    P_B.stop()
