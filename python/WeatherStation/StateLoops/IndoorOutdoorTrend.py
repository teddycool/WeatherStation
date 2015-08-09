__author__ = 'teddycool'
from StateLoopBase import StateLoopBase
import pygame
from WeatherStationConfig import config

class IndoorOutdoorTrend(StateLoopBase):
    def __init__(self):
        super(IndoorOutdoorTrend, self).__init__()
        return

    def initialize(self, sensors):
        #Lables and buttons
        self.headlinelable =  self.myNormalFont.render("Trender senaste dygnet:", 1, config["Colors"]["Lables"])
        self.outdoortemplable = self.myMediumFont.render("Ute:", 1, config["Colors"]["Lables"])
        self.indoortemplable = self.myMediumFont.render("Inne:", 1, config["Colors"]["Lables"])


    def update(self):
        #Check for button pressed and return new state
        #update all relevant data for MainLoop
        #self.outdoortempvalues= self.myNormalFont.render(" - ", 1, config["Colors"]["Lables"])
        return


    def draw(self, screen, sensors):

        pygame.draw.rect(screen,(255,0,0),pygame.Rect(0, 0, 320, 240),5 )
        screen.blit(self.headlinelable, (10,5))
        screen.blit(self.outdoortemplable, (10,30))
        screen.blit(self.indoortemplable, (10,120))

        return screen