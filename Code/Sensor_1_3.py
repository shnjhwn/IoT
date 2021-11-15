### Sound Sensor ###
import RPi.GPIO as GPIO
import time

from mcp3208 import MCP3208

ADC = MCP3208()

ADC_PIN = 0
# 0: Sound Sensor

while True:
    if ADC.read(ADC_PIN) < 2000 :
        # for i in range(8):
        #    print i, "ch Value: ", ADC.read(ADC_PIN)
        print "Sound Detected!"
	
        time.sleep(0.5)

