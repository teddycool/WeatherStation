__author__ = 'teddycool'
import pygame
from StateLoop import StateLoop
from GuiComponents import Button
from WeatherStationConfig import config

class MaxMinState(StateLoop):
    def __init__(self):
        super(MaxMinState, self).__init__()
        return

    def initialize(self):
        #Init buttons etc for MainLoop
        self.exitbutton = Button.Button((20,210,50, 10))
        self.exitbutton.color=(0,255,0)
        self.exitbutton.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.exitbutton.text= config["Texts"]["cancel"]
        self.outdoortemplable = self.myFont.render("Ute:", 1, (255,255,255))
        self.indoortemplable = self.myFont.render("Inne:", 1, (255,255,255))

        return

    def update(self, screen):
        #update all relevant data for MainLoop
        return screen

    def draw(self, screen):
        #Draw main screen
        super(MaxMinState, self).draw(screen)
        screen.blit(self.outdoortemplable, (10,5))
        screen.blit(self.indoortemplable, (170,5))
        self.exitbutton.draw(screen)

        return screen