__author__ = 'teddycool'
#State-switching and handling of general rendering
import pygame
import time
import sys
from StateLoops import CurrentValues
from Sensors import Sensors
from StateLoops import MaxMin
from StateLoops import OutdoorTrend
from StateLoops import FridgeFreezerTrend
from StateLoops import SaverScreen
from WeatherStationConfig import config
from Server import Server


class MainLoop(object):
    def __init__(self):
        #TODO: fix dynamic backlight depending on screentype and (later) lightsensor
        #self._lightcontrolPwm = pwm
        #self._lightcontrolPwm.ChangeDutyCycle(10) #Setting backlight to 20%
        #print "setting pwm dutycycle to 10%"
        self._sensors=Sensors.Sensors()
        self._server= Server.Server()
        self._currentState = CurrentValues.CurrentValues()
        self._maxMin = MaxMin.MaxMin()
        self._outdoorTrend = OutdoorTrend.OutdoorTrend()
        self._fridgeFreezerTrend = FridgeFreezerTrend.FridgeFreezerTrend()
        self._saverScreen = SaverScreen.SaverScreen()
        self._state = {"CurrentValues": self._currentState, "MaxMin": self._maxMin, "OutdoorTrend":self._outdoorTrend, "FridgeFreezerTrend":self._fridgeFreezerTrend, "SaverScreen":self._saverScreen}
        self._currentState = self._state["SaverScreen"]
        self._lastSensorUpdate = 0
        self._lastServerPush = 0
        return

    def initialize(self):
        print "Main init..."
        self.time=time.time()
        #Init all states
        for key in self._state.keys():
            self._state[key].initialize(self._sensors)
        self._sensors.initialize()
        print "Station started at ", self.time

    def update(self,screen, pos):
        #TODO: Add range check
        if time.time() - self._lastSensorUpdate > config["UpdateInterval"]["Sensors"]:
            self._sensors.update()
            self._lastSensorUpdate = time.time()
        if time.time() - self._lastServerPush > config["UpdateInterval"]["Server"]:
            self._server.push(self._sensors)
            self._lastServerPush = time.time()

        newstate = self._currentState.update(pos)
        if newstate != None:
            self._changeState(newstate)

    def draw(self, screen):
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