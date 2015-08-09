__author__ = 'teddycool'
from StateLoopBase import StateLoopBase
import pygame
from GuiComponents import Button
from WeatherStationConfig import config

class FridgeFreezerTrend(StateLoopBase):
    def __init__(self):
        super(FridgeFreezerTrend, self).__init__()
        return

    def initialize(self, sensors):
        self.currentValues = Button.Button((20,210,50, 10))
        self.currentValues.color=(0,255,0)
        self.currentValues.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.currentValues.text= "Aktuella"
        self.headlinelable =  self.myNormalFont.render("Trender senaste dygnet:", 1, config["Colors"]["Lables"])
        self.fridgetempuplable = self.myMediumFont.render("Ovre delen av kylen:", 1, config["Colors"]["Lables"])
        self.fridgetempdownlable = self.myMediumFont.render("Nedre delen av kylen:", 1, config["Colors"]["Lables"])
        self.freezertemplable = self.myMediumFont.render("Frysen:", 1, config["Colors"]["Lables"])
        self._fridgeTrendlist = self.prepareTrendList(sensors.sensorvaluesdict["FridgeTempUpper"]["TrendList"])


    def update(self,mousepressedpos):
        if self.currentValues.selected(mousepressedpos):
            return "CurrentValues"
        return None


    def draw(self, screen, sensors):

        pygame.draw.rect(screen,(255,0,0),pygame.Rect(0, 0, 320, 240),5 )
        self.drawTrend(screen, self._fridgeTrendlist,55,4,10,(0,255,0))
        screen.blit(self.headlinelable, (10,5))
        screen.blit(self.fridgetempuplable, (10,30))
        screen.blit(self.fridgetempdownlable, (10, 90))
        screen.blit(self.freezertemplable, (10,150))
        self.currentValues.draw(screen)
        return screen