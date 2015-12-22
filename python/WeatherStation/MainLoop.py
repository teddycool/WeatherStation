__author__ = 'teddycool'
#State-switching and handling of general rendering
import pygame
import time
import sys
from Sensors import Sensors
from WeatherStationConfig import config
from Server import Server
from Actuators import LedIndicator
import RPi.GPIO as GPIO
from Inputs import IoInputs


class MainLoop(object):
    def __init__(self):
        self._sensors=Sensors.Sensors()
        self._server = Server.Server()
        GPIO.setmode(GPIO.BCM)
        #TODO MOVE leds and buttons to sensor update and alarm module
        self._sensorLed = LedIndicator.LedIndicator(GPIO, 12)
        self._hushBtn = IoInputs.PushButton(GPIO, 26)
        self._lastSensorUpdate = 0
        self._lastServerPush = 0
        return

    def initialize(self):
        print "Main init..."
        self.time=time.time()
        self._sensors.initialize()
        print "Station started at ", self.time

    def update(self):
        #print "MainLoop update..."
        self._sensorLed.update()
        self._hushBtn.update()
        if time.time() - self._lastSensorUpdate > config["UpdateInterval"]["Sensors"]:
            self._sensors.update()
            self._lastSensorUpdate = time.time()
            #Turn on indication for sensor update
            self._sensorLed.activate(True)
            print self._sensors.toString()
        if time.time() - self._lastServerPush > config["UpdateInterval"]["Server"]:
            self._server.push(self._sensors)
            self._lastServerPush = time.time()
        time.sleep(1)

