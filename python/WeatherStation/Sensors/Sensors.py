__author__ = 'teddycool'
import os
from WeatherStationConfig import config
import time
import pickle
#Simple sensor-mock for easier development when running on PC
#Import neededsensor-classes
if  os.sys.platform != 'win32':
    import DS18B20
    import DHT
    import BMP
    import SHT
else:
    import random
import sys

class Sensors(object):
    def __init__(self):
        #init the needed sensors, one sensor can have many values
        if  os.sys.platform != 'win32':
            self._fridgeSensorUpper = DS18B20.DS18B20("28-031515b906ff")
            self._fridgeSensorLower = DS18B20.DS18B20("28-031515ac6eff")
            self._freezerSensor  =    DS18B20.DS18B20("28-021550136cff")

            #TODO: check settings and calibration
            self._indoor = DHT.DHT('11',17)
            self._outdoorBar = BMP.BMP()
            self._outdoorHum = SHT.SHT21(1)

        try:
           self.sensorvaluesdict = pickle.load(open('valuesdict.pickle','rb'))
           print "Loaded values dictionary...."
        except:
            #Print to log...
            #e = sys.exc_info()[0]
            #print str(e)
            import copy
            self.sensorvaluesdict={}
            valuesdict = {"Current": 0, "TrendList": []}
            measurements = ["IndoorTemp","OutdoorTemp", "IndoorHum", "OutdoorHum", "OutdoorBar","FridgeTempUpper", "FridgeTempLower", "FreezerTemp"]
            for meassure in measurements:
                self.sensorvaluesdict[meassure]= copy.deepcopy(valuesdict)
            print "Created values dictionary..."

    def initialize(self):
        return

    def update(self):
         self._updateValues()

    def _updateValues(self):
        print "Updating sensor values start: " + str(time.time())
        if  os.sys.platform != 'win32':
            #TODO: Check that values are reasonable
            indoor = self._indoor.read()
            self.sensorvaluesdict["FridgeTempUpper"]["Current"] = self._fridgeSensorUpper.read_temp()
            self.sensorvaluesdict["FridgeTempLower"]["Current"] = self._fridgeSensorLower.read_temp()
            self.sensorvaluesdict["FreezerTemp"]["Current"] = self._freezerSensor.read_temp()
            self.sensorvaluesdict["OutdoorBar"]["Current"] = self._outdoorBar.readPressure()
            self.sensorvaluesdict["IndoorHum"]["Current"] = indoor[0]
            self.sensorvaluesdict["IndoorTemp"]["Current"] = indoor[1]
            self.sensorvaluesdict["OutdoorHum"]["Current"] = self._outdoorHum.read_humidity()
            self.sensorvaluesdict["OutdoorTemp"]["Current"] = self._outdoorHum.read_temperature()
        else:
            #simple mock for gui development
            self.sensorvaluesdict["FridgeTempUpper"]["Current"] = str(round(random.uniform(5,10),1))
            self.sensorvaluesdict["FridgeTempLower"]["Current"] = str(round(random.uniform(5,10),1))
            self.sensorvaluesdict["FreezerTemp"]["Current"] = str(round(random.uniform(-22,-5),1))
            self.sensorvaluesdict["IndoorHum"]["Current"] = str(round(random.uniform(10,90),1))
            self.sensorvaluesdict["IndoorTemp"]["Current"] = str(round(random.uniform(17,25),1))
            self.sensorvaluesdict["OutdoorHum"]["Current"] = str(round(random.uniform(10,90),1))
            self.sensorvaluesdict["OutdoorTemp"]["Current"] = str(round(random.uniform(-20,25),1))
            self.sensorvaluesdict["OutdoorBar"]["Current"] = str(round(random.uniform(90,102),1))
        for key in self.sensorvaluesdict:
            self.sensorvaluesdict[key]["TrendList"] = self._updateValuesList(self.sensorvaluesdict[key]["Current"], self.sensorvaluesdict[key]["TrendList"] )
        pickle.dump(self.sensorvaluesdict,open('valuesdict.pickle','wb'))
        print "Dumping current valuesdict to disk"
        print "Updating sensor values finished: " + str(time.time())

    def _updateValuesList(self,value, valuelist):
        #TODO: add timestamp?
        if value != "N/A":
            valuelist.append(float(value))
            if (len(valuelist)> config["MaxSavedValues"]):
                poped = valuelist.pop(0)
                print "Value poped from valuelist: " + str(poped)
        return valuelist

    def urlString(self):
        url = "?time=" + time.strftime("%Y-%m-%d %H:%M:%S") + "&"
        for key in self.sensorvaluesdict:
            value = self.sensorvaluesdict[key]["Current"]
            if value != "N/A":
                url = url + key + "=" + value + "&"
        return url[:-1] #remove last '&'