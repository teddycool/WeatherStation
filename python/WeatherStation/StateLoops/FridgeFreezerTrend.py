__author__ = 'teddycool'
from StateLoopBase import StateLoopBase
import pygame
from GuiComponents import Button
from WeatherStationConfig import config
import time

class FridgeFreezerTrend(StateLoopBase):
    def __init__(self):
        super(FridgeFreezerTrend, self).__init__()
        return

    def initialize(self, sensors):
        self.currentValuesBtn = Button.Button((240,20,70, 10))
        self.currentValuesBtn.color=(0,255,0)
        self.currentValuesBtn.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.currentValuesBtn.text= "Tillbaka->"

        self.headlinelable =  self.myNormalFont.render("Senaste trender:", 1, config["Colors"]["Lables"])
        self.fridgetempuplable = self.myMediumFont.render("Ovre delen av kylen:", 1, config["Colors"]["Lables"])
        self.fridgetempdownlable = self.myMediumFont.render("Nedre delen av kylen:", 1, config["Colors"]["Lables"])
        self.freezertemplable = self.myMediumFont.render("Frysen:", 1, config["Colors"]["Lables"])

        #prepare values in list for trend drawing
        self._fridgeTrendUplist = self.createTrendList(sensors.sensorvaluesdict["FridgeTempUpper"]["TrendList"])
        self._fridgeTrendDownlist = self.createTrendList(sensors.sensorvaluesdict["FridgeTempLower"]["TrendList"])
        self._frezeerlist = self.createTrendList(sensors.sensorvaluesdict["FreezerTemp"]["TrendList"])

        self._last_active = time.time()


    def update(self,mousepressedpos):
        if time.time()-self._last_active > config["UpdateInterval"]["Saver"]:
            return "SaverScreen"
        if self.currentValuesBtn.selected(mousepressedpos):
            return "CurrentValues"
        else:
            return None


    def draw(self, screen, sensors):

        #pygame.draw.rect(screen,(255,0,0),pygame.Rect(0, 0, 320, 240),5 )

        #Headline and return button
        screen.blit(self.headlinelable, (10,5))
        self.currentValuesBtn.draw(screen)

        #Trends, hl
        screen.blit(self.fridgetempuplable, (10,40))
        #Trends, draw values
        self.drawTrend(screen, self._fridgeTrendUplist,55,95,(0,255,0))

        screen.blit(self.fridgetempdownlable, (10,100))
        self.drawTrend(screen, self._fridgeTrendDownlist,115,155,(0,255,0))

        screen.blit(self.freezertemplable, (10,170))
        self.drawTrend(screen, self._frezeerlist,190,230,(0,255,0))

        return screen