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


class MainLoop(object):
    def __init__(self):
        self._sensors=Sensors.Sensors()
        self._server = Server.Server()
        self._led = LedIndicator.LedIndicator(GPIO, 12)
        self._lastSensorUpdate = 0
        self._lastServerPush = 0
        return

    def initialize(self):
        print "Main init..."
        self.time=time.time()
        self._sensors.initialize()
        print "Station started at ", self.time

    def update(self):
        print "MainLoop update..."
        self._led.update()
        if time.time() - self._lastSensorUpdate > config["UpdateInterval"]["Sensors"]:
            self._sensors.update()
            self._lastSensorUpdate = time.time()
            #Turn on indication for sensor update
            self._led.activate(True)
        if time.time() - self._lastServerPush > config["UpdateInterval"]["Server"]:
            self._server.push(self._sensors)
            self._lastServerPush = time.time()

