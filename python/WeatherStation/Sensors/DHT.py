__author__ = 'teddycool'
#https://learn.adafruit.com/downloads/pdf/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.pdf
import os
import time
import Adafruit_DHT
class DHT(object):

    def __init__(self, type, pin):
        self._pin = pin
        sensor_args = { '11': Adafruit_DHT.DHT11,
				'22': Adafruit_DHT.DHT22,
				'2302': Adafruit_DHT.AM2302 }
        self._sensor = sensor_args[type]


    def read(self):
        #humidity, temperature
        return Adafruit_DHT.read_retry(self._sensor, self._pin)




if __name__ == '__main__':
    print "Testcode for DHT temp and humidity sensors"
    dht11=DHT('11',17)
    print dht11.read()
    dht22=DHT('22',4)
    print dht22.read()