__author__ = 'teddycool'
import pygame
from StateLoopBase import StateLoopBase
from GuiComponents import Button
from WeatherStationConfig import config

class MaxMin(StateLoopBase):
    def __init__(self):
        super(MaxMin, self).__init__()
        return

    def initialize(self, sensors):
        #Init buttons etc for MainLoop
        self.exitbutton = Button.Button((20,210,50, 10))
        self.exitbutton.color=(0,255,0)
        self.exitbutton.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.exitbutton.text= "->Tillbaka"
        self.outdoortemplable = self.myNormalFont.render("Ute:", 1, (255,255,255))
        self.indoortemplable = self.myNormalFont.render("Inne:", 1, (255,255,255))

        return

    def update(self, screen):
        #update all relevant data for MainLoop
        return screen

    def draw(self, screen):
        #Draw main screen
        super(MaxMin, self).draw(screen)
        screen.blit(self.outdoortemplable, (10,5))
        screen.blit(self.indoortemplable, (170,5))
        self.exitbutton.draw(screen)

        return screen