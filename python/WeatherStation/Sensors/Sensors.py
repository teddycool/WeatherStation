__author__ = 'teddycool'

import DS18B20

class Sensors(object):
    def __init__(self):
        #init the needed sensors, one sensor can have many values
        self._fridgeSensor1 = DS18B20.DS18B20("28-03146af27cff")
        return

    def initialize(self):
        #connect each variable to the sensor and value
        self.indoorTemp = 20
        self.outdoorTemp = 10
        self.indoorHum = 80
        self.outdoorHum = 70
        self.outdoorBar = 1024
        self.fridgeTemp = 5
        self.freezerTemp = -18
        return

    def update(self):
        self.fridgeTemp = self._fridgeSensor1.read_temp()[0]
        return
