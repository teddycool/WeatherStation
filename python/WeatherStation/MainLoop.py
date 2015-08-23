__author__ = 'teddycool'
#State-switching and handling of general rendering
import pygame
from pygame.locals import *
import time
import sys
from StateLoops import CurrentValues
from Sensors import Sensors
from StateLoops import MaxMin
from StateLoops import IndoorOutdoorTrend
from StateLoops import FridgeFreezerTrend
from WeatherStationConfig import config
from Server import Server

class MainLoop(object):
    def __init__(self):
        self._sensors=Sensors.Sensors()
        self._server= Server.Server()
        self._currentState = CurrentValues.CurrentValues()
        self._maxMin = MaxMin.MaxMin()
        self._indoorOutdoorTrend = IndoorOutdoorTrend.IndoorOutdoorTrend()
        self._fridgeFreezerTrend = FridgeFreezerTrend.FridgeFreezerTrend()
        self._state = {"CurrentValues": self._currentState, "MaxMin": self._maxMin, "IndoorOutdoorTrend":self._indoorOutdoorTrend, "FridgeFreezerTrend":self._fridgeFreezerTrend}
        self._currentState = self._state["CurrentValues"]
        self._lastSensorUpdate = 0
        self._lastServerPush = 0
        self._lastScreenUpdate = 0
        return

    def initialize(self):
        print "Main init..."
        self.time=time.time()
        #Init all states
        for key in self._state.keys():
            self._state[key].initialize(self._sensors)
        self._sensors.initialize()
        print "Station started at ", self.time

    def update(self,screen):
        pos=(0,0)
        if time.time() - self._lastSensorUpdate > config["UpdateInterval"]["Sensors"]:
            self._sensors.update()
            self._lastSensorUpdate = time.time()
        if time.time() - self._lastServerPush > config["UpdateInterval"]["Server"]:
            self._server.push(self._sensors)
            self._lastServerPush = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if(event.type is MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
        newstate = self._currentState.update(pos)
        if newstate != None:
            self._changeState(newstate)
        return

    def draw(self, screen):
        if time.time() - self._lastSensorUpdate > config["UpdateInterval"]["Screen"]:
            black=0,0,0
            screen.fill(black)
            self._currentState.draw(screen, self._sensors)
        return screen

    def _changeState(self, newstate):
        if newstate not in self._state:
            self._currentState = CurrentValues.CurrentValues()
        else:
            if self._currentState != self._state[newstate]:
                self._currentState = self._state[newstate]
                self._currentState.initialize(self._sensors)
        return newstate