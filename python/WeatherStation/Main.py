__author__ = 'teddycool'

import time
import MainLoop
from WeatherStationConfig import config
#import RPi.GPIO as GPIO
class Main(object):

    def __init__(self):

        print "Init Main object..."
        self._mainLoop=MainLoop.MainLoop()

    def run(self):
        print "Start run-loop..."
        self._mainLoop.initialize()
        running = True
        while running:
            self._mainLoop.update()
            time.sleep(0.5)