__author__ = 'teddycool'
#PREREQ: https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/using-the-adafruit-bmp-python-library
try:
    import Adafruit_BMP.BMP085 as BMP085
except:
    pass


class BMP(object):

    def __init__(self):
        try:
            self._sensor = BMP085.BMP085()
            self._init=True
        except:
            self._init = False


    def readPressure(self):
        if self._init:
            try:
                pre = float('{0:0.2f}'.format(self._sensor.read_pressure()/1000.0))
                return str(round(pre,1))
            except:
                return "N/A"
        else:
            return "N/A"

    def readTemperature(self):
        if self._init:
            try:
                temp = float('{0:0.2f}'.format(self._sensor.read_temperature()))
                return str(round(temp,1))
            except:
                return "N/A"
        else:
            return "N/A"


if __name__ == '__main__':
    print "Testcode for BMP085 barometric"
    bmp = BMP()
    pres = bmp.readPressure()
    temp= bmp.readTemperature()
    print str(pres) + "hPa " + str(temp) + "C "