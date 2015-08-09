__author__ = 'teddycool'
import os
from WeatherStationConfig import config

#Simple sensor-mock for easier development when running on PC
#Import neededsensor-classes
if  os.sys.platform != 'win32':
    import DS18B20
else:
    import random

class Sensors(object):
    def __init__(self):
        #init the needed sensors, one sensor can have many values
        if  os.sys.platform != 'win32':
            self._fridgeSensorUpper = DS18B20.DS18B20("28-03146af27cff")
            #self._fridgeSensorLower = DS18B20.DS18B20("28-03146af27cff")

        import copy
        self.sensorvaluesdict={}
        valuesdict = {"Current": 0, "TrendList": []}
        measurements = ["IndoorTemp","OutdoorTemp", "IndoorHum", "OutdoorHum", "OutdoorBar","FridgeTempUpper", "FridgeTempLower", "FreezerTemp"]
        for meassure in measurements:
            self.sensorvaluesdict[meassure]= copy.deepcopy(valuesdict)
        return

    def initialize(self):
        #connect each variable to the sensor and value


        self._updateValues()
        return

    def update(self):
         self._updateValues()
         return

    def _updateValues(self):
        if  os.sys.platform != 'win32':
            self.sensorvaluesdict["FridgeTempUpper"]["Current"] = self._fridgeSensorUpper.read_temp()[0]
            self.sensorvaluesdict["FridgeTempUpper"]["TrendList"] = self._updateValuesList(self.sensorvaluesdict["FridgeTempUpper"]["Current"], self.sensorvaluesdict["FridgeTempUpper"]["TrendList"] )
        else:
            self.sensorvaluesdict["FridgeTempUpper"]["Current"] = random.uniform(15,22)
            self.sensorvaluesdict["FridgeTempUpper"]["TrendList"] = self._updateValuesList(self.sensorvaluesdict["FridgeTempUpper"]["Current"], self.sensorvaluesdict["FridgeTempUpper"]["TrendList"] )


        return

    def _updateValuesList(self,value, valuelist):
        valuelist.append(value)
        if (len(valuelist)> config["MaxSavedValues"]):
            valuelist.pop(0)
        return valuelist

