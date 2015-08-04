__author__ = 'teddycool'
#State-switching and handling of general rendering
import pygame
import time


class MainLoop(object):
    def __init__(self):
        #self._inputs=Inputs.Inputs(self)
        #self._calibrateState = CamCalibrateLoop.CamCalibrateLoop()
        #self._mountingState = CamMoutningLoop.CamMountingLoop()
        #self._playState = PlayStateLoop.PlayStateLoop()
        #self._state = {"MountState": self._mountingState, "CalState": self._calibrateState, "PlayState": self._playState}
        #self._currentStateLoop = self._state["MountState"]
        return

    def initialize(self):
        print "Main init..."
        #self._inputs.initialize()
        self.time=time.time()
        #Init all states
        #for key in self._state.keys():
        #    self._state[key].initialize()
        print "Station started at ", self.time

    def update(self,screen):
        return

    def draw(self, screen):

        return screen

    def changeState(self, newstate):
        if (newstate == 0) or (newstate == "InitState"):
            self._currentStateLoop = CamCalibrateLoop.CamCalibrateLoop()

        self._currentStateLoop.initialize()
        return newstate