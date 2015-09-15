__author__ = 'teddycool'

__author__ = 'teddycool'
from StateLoopBase import StateLoopBase
import pygame
from GuiComponents import Button
from WeatherStationConfig import config
import time

class OutdoorTrend(StateLoopBase):
    def __init__(self):
        super(OutdoorTrend, self).__init__()
        return

    def initialize(self, sensors):
        self.currentValuesBtn = Button.Button((240,20,70, 10))
        self.currentValuesBtn.color=(0,255,0)
        self.currentValuesBtn.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.currentValuesBtn.text= "Tillbaka->"

        self.headlinelable =  self.myNormalFont.render("Senaste trender:", 1, config["Colors"]["Lables"])
        self.outdoortemplable = self.myMediumFont.render("Temperatur:", 1, config["Colors"]["Lables"])
        self.outdoorbarlable = self.myMediumFont.render("Lufttryck:", 1, config["Colors"]["Lables"])
        self.outdoorhumlable = self.myMediumFont.render("Luftfuktighet:", 1, config["Colors"]["Lables"])

        #prepare values in list for trend drawing
        self._outdoortemplist = self.createTrendList(sensors.sensorvaluesdict["OutdoorTemp"]["TrendList"])
        self._outdoorbarlist = self.createTrendList(sensors.sensorvaluesdict["OutdoorBar"]["TrendList"])
        self._outdoorhumlist = self.createTrendList(sensors.sensorvaluesdict["OutdoorHum"]["TrendList"])

        self._last_active = time.time()


    def update(self,mousepressedpos):
        if time.time()-self._last_active > config["UpdateInterval"]["Saver"]:
            return "SaverScreen"
        if self.currentValuesBtn.selected(mousepressedpos):
            return "CurrentValues"
        else:
            return None


    def draw(self, screen, sensors):

        #Headline and return button
        screen.blit(self.headlinelable, (10,5))
        self.currentValuesBtn.draw(screen)

        screen.blit(self.outdoortemplable, (10,40))
        self.drawTrend(screen, self._outdoortemplist,55,95,(0,255,0))

        screen.blit(self.outdoorbarlable, (10,115))
        self.drawTrend(screen, self._outdoorbarlist,130,170,(0,255,0))

        screen.blit(self.outdoorhumlable, (10,185))
        self.drawTrend(screen, self._outdoorhumlist,200,240,(0,255,0))

        return screen