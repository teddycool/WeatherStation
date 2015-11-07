__author__ = 'teddycool'
from StateLoopBase import StateLoopBase
from GuiComponents import Button
from WeatherStationConfig import config
import time

class SaverScreen(StateLoopBase):
    def __init__(self):
        super(SaverScreen, self).__init__()
        return

    def initialize(self, sensors):
        self._last_active = time.time()
        return


    def update(self, mousepressedpos):
        #TODO: add range sensor for turning off and on screen...
       # if time.time()-self._last_active > config["UpdateInterval"]["Range"]:
            #Turn off screen
        if mousepressedpos != (0,0):
            return "CurrentValues"


    def draw(self, screen, sensors):
        #datestring = time.strftime("%Y-%m-%d")
        timestring = time.strftime("%H:%M")
        outdoorstring = str(sensors.sensorvaluesdict["OutdoorTemp"]["Current"]) + " C"
        outdoortemp = self.myLargeFont.render( outdoorstring, 1, config["Colors"]["SaverText"])
        clocktime = self.myLargeFont.render(timestring, 1, config["Colors"]["SaverText"])
        owidth = self.myLargeFont.size(outdoorstring)[0]
        twidth = self.myLargeFont.size(timestring)[0]
        screen.blit(outdoortemp, ((320-owidth)/2,30))
        screen.blit(clocktime, ((320-twidth)/2, 120))