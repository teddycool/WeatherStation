__author__ = 'teddycool'
import os
from WeatherStationConfig import config
import time
import pickle
from Actuators import LedIndicator
#Simple sensor-mock for easier development when running on PC
#Import neededsensor-classes
if  os.sys.platform != 'win32':
    import DS18B20
    import DHT
    import BMP
    import SHT
    import TSL2561
else:
    import random
import sys

class Sensors(object):
    def __init__(self, GPIO):

        #init the needed sensors, one sensor can have many values

        self._fridgeSensorUpper = DS18B20.DS18B20("28-031515b906ff")
        self._fridgeSensorLower = DS18B20.DS18B20("28-031515ac6eff")
        self._freezerSensor  =    DS18B20.DS18B20("28-021550136cff")

        #TODO: check settings and calibration
        self._indoor = DHT.DHT('11',21)
        self._outdoorBar = BMP.BMP()
        self._outdoorHum = SHT.SHT21(1)
        self._light = TSL2561.TSL2561()

        try:
           self.sensorvaluesdict = pickle.load(open('valuesdict.pickle','rb'))
           print "Loaded values dictionary...."
        except:
            import copy
            self.sensorvaluesdict={}
            valuesdict = {"Current": 0, "TrendList": []}
            measurements = ["IndoorTemp","OutdoorTemp", "IndoorHum", "OutdoorHum", "OutdoorBar","FridgeTempUpper", "FridgeTempLower", "FreezerTemp", "ALight", "IrLight"]
            for meassure in measurements:
                self.sensorvaluesdict[meassure]= copy.deepcopy(valuesdict)
            print "Created values dictionary..."

    def initialize(self):
        return

    def update(self):

        self._updateValues()

    def _updateValues(self):
        print "Updating sensor values start: " + str(time.time())
        #TODO: Check that values are reasonable
        #TODO: Add one timestamp for all readings [sensors][time]
        indoor = self._indoor.read()
        self.sensorvaluesdict["FridgeTempUpper"]["Current"] = self._fridgeSensorUpper.read_temp()
        self.sensorvaluesdict["FridgeTempLower"]["Current"] = self._fridgeSensorLower.read_temp()
        self.sensorvaluesdict["FreezerTemp"]["Current"] = self._freezerSensor.read_temp()
        self.sensorvaluesdict["OutdoorBar"]["Current"] = self._outdoorBar.readPressure()
        self.sensorvaluesdict["IndoorHum"]["Current"] = indoor[0]
        self.sensorvaluesdict["IndoorTemp"]["Current"] = indoor[1]
        self.sensorvaluesdict["OutdoorHum"]["Current"] = self._outdoorHum.read_humidity()
        self.sensorvaluesdict["OutdoorTemp"]["Current"] = self._outdoorHum.read_temperature()

        #TODO fix readings and update class for light...
        self.sensorvaluesdict["ALight"]["Current"] = str(round(self._light.readIR(),1))
        self.sensorvaluesdict["IrLight"]["Current"] = self._light.readLux()

        for key in self.sensorvaluesdict:
            self.sensorvaluesdict[key]["TrendList"] = self._updateValuesList(self.sensorvaluesdict[key]["Current"], self.sensorvaluesdict[key]["TrendList"] )
        pickle.dump(self.sensorvaluesdict,open('valuesdict.pickle','wb'))
        print "Dumping current valuesdict to file"
        print "Updating of sensor values finished: " + str(time.time())

    def _updateValuesList(self,value, valuelist):
        #Turn on indication for sensor update
        #TODO: add timestamp?
        if value != "N/A":
            valuelist.append(float(value))
            if (len(valuelist)> config["MaxSavedValues"]):
                poped = valuelist.pop(0)
                print "Value poped from valuelist: " + str(poped)
        return valuelist

    def urlString(self, table='short'):
        #TODO: fix timestamp to be actual measuring time
        url = "?table=" + table + "&time=" + time.strftime("%Y-%m-%d %H:%M:%S") + "&"
        for key in self.sensorvaluesdict:
            value = self.sensorvaluesdict[key]["Current"]
            if value != "N/A":
                url = url + key + "=" + value + "&"
        return url[:-1] #remove last '&'

    def toString(self):
        str = ""
        for key in self.sensorvaluesdict:
            value = self.sensorvaluesdict[key]["Current"]
            str = str + key + "=" + value + ", "
        return str[:-2]