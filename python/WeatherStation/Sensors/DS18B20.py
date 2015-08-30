__author__ = 'teddycool'
#http://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi
import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

class DS18B20(object):
    
    def __init__(self, serial):
        self._serial = serial
        self._sensorfile= "/sys/bus/w1/devices/" + self._serial + "/w1_slave"

    def temp_raw(self):    
        f = open(self._sensorfile, 'r')
        lines = f.readlines()
        f.close()
        return lines
    
    def read_temp(self):
        try:
            lines = self.temp_raw()
            while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = self.temp_raw()

            temp_output = lines[1].find('t=')

            if temp_output != -1:
                temp_string = lines[1].strip()[temp_output+2:]
                temp_c = float(temp_string) / 1000.0
                return str(round(temp_c,1))
        except:
            return "N/A"



if __name__ == '__main__':
    print "Testcode for DS18B20"
    serial = "28-031515b906ff"
    serial2= "28-031515ac6eff"
    print "Serials: " + serial + " " + serial2
    ts=DS18B20(serial)
    ts2 = DS18B20(serial2)
    print(ts.read_temp())
    print (ts2.read_temp())
    print(ts.temp_raw())
    print(ts2.temp_raw())



