__author__ = 'teddycool'
#State-switching and handling of general rendering
import pygame
import time
from StateLoops import CurrentState
from Sensors import Sensors
from StateLoops import MaxMinState
from WeatherStationConfig import config
from Server import Server

class MainLoop(object):
    def __init__(self):

        self._sensors=Sensors.Sensors()
        #self._sensors= None
        self._server= Server.Server()
        self._currentStateLoop = CurrentState.CurrentState()
        self._maxminStateLoop = MaxMinState.MaxMinState()
        self._state = {"CurrentState": self._currentStateLoop, "MaxMinState": self._maxminStateLoop}
        self._currentStateLoop = self._state["CurrentState"]
        self._lastSensorUpdate = 0
        self._lastServerPush = 0
        return

    def initialize(self):
        print "Main init..."
        self.time=time.time()
        #Init all states
        for key in self._state.keys():
            self._state[key].initialize()
        print "Station started at ", self.time

    def update(self,screen):
        if time.time() - self._lastSensorUpdate > config["UpdateInterval"]["Screen"]*1000:
           self._sensors.update()
        if time.time() - self._lastServerPush > config["UpdateInterval"]["Server"]*1000:
            self._server.push(self._sensors)
        self._currentStateLoop.update(screen)
        return

    def draw(self, screen):
        self._currentStateLoop.draw(screen, self._sensors)
        return screen

    def changeState(self, newstate):
        if (newstate == 0) or (newstate == "CurrentState"):
            self._currentStateLoop = CurrentState.CurrentState()

        self._currentStateLoop.initialize()
        return newstate