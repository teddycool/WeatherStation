__author__ = 'psk'

import Adafruit_BMP.BMP085 as BMP085


class BMP(object):

    def __init__(self):
        self._sensor = BMP085.BMP085()


    def readPressure(self):
        return float('{0:0.2f}'.format(self._sensor.read_pressure()/100.0))

    def readTemperature(self):
        return float('{0:0.2f}'.format(self._sensor.read_temperature()))


if __name__ == '__main__':
    print "Testcode for BMP085 barometric"
    bmp = BMP()
    pres = bmp.readPressure()
    temp= bmp.readTemperature()
    print str(pres) + "hPa " + str(temp) + "C "