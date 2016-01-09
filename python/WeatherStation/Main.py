__author__ = 'teddycool'

import os, sys, pygame
from pygame.locals import *
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
            try:
                self._mainLoop.update()
            except Exception as e:
                running = False
                print str(e)
                #self._lightcontrolPwm.ChangeDutyCycle(100)
                #self._lightcontrolPwm.stop()
                #GPIO.cleanup()

#Testcode to run module. Standard Python way of testing modules.

if __name__ == "__main__":

    weatherstationloop=Main()
    weatherstationloop.run()
