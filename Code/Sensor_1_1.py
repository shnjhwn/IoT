### 1_1 Temerature and Humidity Sensor

### prepare in advance ###

# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# cd Adafruiot_Python_DHT
# sudo apt-get update
# sudo apt-get install build-essential python-dev
# sudo python setup.py install

##########################

import Adafruit_DHT as dht
from time import sleep

# set DATA pin
DHT_PIN = 7

while True:
    # Read Temp and Hum from DHT22
    h, t = dht.read_retry(dht.DHT22, DHT_PIN)
    # print Temperature and Humidity on Shell window
    print "----------Value----------"
    print "Temperature: ", t, "*C"
    print "Humidity   : ", h, "%"
    sleep(0.5) # Wait 2 seconds and read again
