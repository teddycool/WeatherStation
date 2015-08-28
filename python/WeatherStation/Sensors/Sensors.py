__author__ = 'teddycool'
import os
from WeatherStationConfig import config
import time
#Simple sensor-mock for easier development when running on PC
#Import neededsensor-classes
if  os.sys.platform != 'win32':
    import DS18B20
    import DHT
    import BMP
else:
    import random

class Sensors(object):
    def __init__(self):
        #init the needed sensors, one sensor can have many values
        if  os.sys.platform != 'win32':
            self._fridgeSensorUpper = DS18B20.DS18B20("28-03146af27cff")
            self._fridgeSensorLower = DS18B20.DS18B20("28-031515ac6eff")
            self._freezerSensor  = DS18B20.DS18B20("28-021550136cff")

            #TODO: check settings and calibration
            self._indoor = DHT.DHT('11',17)
            self._outdoor = DHT.DHT('22',27)
            self._outdoorBar = BMP.BMP()

        import copy
        self.sensorvaluesdict={}
        valuesdict = {"Current": 0, "TrendList": []}
        measurements = ["IndoorTemp","OutdoorTemp", "IndoorHum", "OutdoorHum", "OutdoorBar","FridgeTempUpper", "FridgeTempLower", "FreezerTemp"]
        for meassure in measurements:
            self.sensorvaluesdict[meassure]= copy.deepcopy(valuesdict)
        return

    def initialize(self):
        #connect each variable to the sensor and value
        #self._updateValues()
        return

    def update(self):
         self._updateValues()
         return

    def _updateValues(self):
        print "Updating sensor values start: " + str(time.time())
        if  os.sys.platform != 'win32':
            #Read values from sensor with more then one returnvalue
            indoor= self._indoor.read()
            outdoor = self._outdoor.read()
            self.sensorvaluesdict["FridgeTempUpper"]["Current"] = self._fridgeSensorUpper.read_temp()[0]
            self.sensorvaluesdict["FridgeTempLower"]["Current"] = self._fridgeSensorLower.read_temp()[0]
            self.sensorvaluesdict["FreezerTemp"]["Current"] = self._freezerSensor.read_temp()[0]
            self.sensorvaluesdict["OutdoorBar"]["Current"] = self._outdoorBar.readPressure()
            self.sensorvaluesdict["IndoorHum"]["Current"] = indoor[0]
            self.sensorvaluesdict["IndoorTemp"]["Current"] = indoor[1]
            self.sensorvaluesdict["OutdoorHum"]["Current"] = outdoor[0]
            self.sensorvaluesdict["OutdoorTemp"]["Current"] = self._outdoorBar.readTemperature()

           # self.sensorvaluesdict["FridgeTempUpper"]["TrendList"] = self._updateValuesList(self.sensorvaluesdict["FridgeTempUpper"]["Current"], self.sensorvaluesdict["FridgeTempUpper"]["TrendList"] )
        else:
            self.sensorvaluesdict["FridgeTempUpper"]["Current"] = random.uniform(5,10)
            self.sensorvaluesdict["FridgeTempLower"]["Current"] = random.uniform(5,10)
            self.sensorvaluesdict["FreezerTemp"]["Current"] = random.uniform(-22,-5)
            self.sensorvaluesdict["IndoorHum"]["Current"] = random.uniform(10,90)
            self.sensorvaluesdict["IndoorTemp"]["Current"] = random.uniform(17,25)
            self.sensorvaluesdict["OutdoorHum"]["Current"] = random.uniform(10,90)
            self.sensorvaluesdict["OutdoorTemp"]["Current"] = random.uniform(-20,25)
            self.sensorvaluesdict["OutdoorBar"]["Current"] = random.uniform(900,1020)
            #TODO: Handle exception when value is not a float (missing value/broken sensor/out of range etc)
        for key in self.sensorvaluesdict:
            self.sensorvaluesdict[key]["Current"] = round(self.sensorvaluesdict[key]["Current"],1)
            self.sensorvaluesdict[key]["TrendList"] = self._updateValuesList(self.sensorvaluesdict[key]["Current"], self.sensorvaluesdict[key]["TrendList"] )
        #self.sensorvaluesdict["IndoorHum"]["TrendList"] = self._updateValuesList(self.sensorvaluesdict["IndoorHum"]["Current"], self.sensorvaluesdict["IndoorHum"]["TrendList"] )
        print "Updating sensor values finished: " + str(time.time())
        return

    def _updateValuesList(self,value, valuelist):
        #TODO: add timestamp?
        valuelist.append(value)
        if (len(valuelist)> config["MaxSavedValues"]):
            valuelist.pop(0)
        return valuelist

