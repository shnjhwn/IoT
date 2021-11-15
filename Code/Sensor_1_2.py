# 1_2 Light Sensor 

## Prepare in advance

### 1. Activate SPI & I2C

### 2. Install build_utils 
# git clone https://github.com/walchko/build_utils
# cd build_utils
# pip install -e

### 3. Install MCP3208 module 
# git clone https://github.com/MomsFriendlyRobotCompany/mcp3208.git
# cd mcp3208
# sudo apt-get update
# sudo apt-get install build-essential python-dev
# sudo python setup.py install

#################################

import RPi.GPIO as GPIO
import time

from mcp3208 import MCP3208

ADC = MCP3208()

ADC_PIN = 1
# 1: Light Sensor

while True:
    for i in range(8):
        print i, "ch Value: ", ADC.read(ADC_PIN)
    time.sleep(0.5)
