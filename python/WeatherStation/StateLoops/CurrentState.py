__author__ = 'teddycool'
import pygame
from StateLoop import StateLoop
from GuiComponents import Button
from WeatherStationConfig import config

class CurrentState(StateLoop):
    def __init__(self):
        super(CurrentState, self).__init__()
        return

    def initialize(self):
        #Init buttons etc for MainLoop
        self.maxminstatebutton = Button.Button((20,210,50, 10))
        self.maxminstatebutton.color=(0,255,0)
        self.maxminstatebutton.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.maxminstatebutton.text= config["Texts"]["maxmin"]
        self.maxminheadlinelable =  self.myFont.render("Aktuella varden just nu:", 1, config["Colors"]["Lables"])
        self.outdoortemplable = self.myFont.render("Ute:", 1, config["Colors"]["Lables"])
        self.indoortemplable = self.myFont.render("Inne:", 1, config["Colors"]["Lables"])
        self.fridgetemplable = self.myFont.render("Kylen:", 1, config["Colors"]["Lables"])
        self.freezertemplable = self.myFont.render("Frysen:", 1, config["Colors"]["Lables"])

        self.indoortempvalues= self.myFont.render(" -- ", 1, config["Colors"]["Values"])
        self.outdoortempvalues= self.myFont.render(" -- ", 1, config["Colors"]["Alarm"])
        self.fridgetempvalues = self.myFont.render(" -- ", 1, config["Colors"]["Values"])
        self.freezertempvalues = self.myFont.render(" -- ", 1, config["Colors"]["Values"])
        return

    def update(self, screen):
        #update all relevant data for MainLoop
        #self.outdoortempvalues= self.myFont.render(" - ", 1, config["Colors"]["Lables"])
        return screen

    def draw(self, screen, sensors):

        #Draw CurrentState screen
        self.fridgetempvalues = self.myFont.render(str(sensors.fridgeTemp) + " C", 1, config["Colors"]["Values"])
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(0, 0, 320, 240),5 )
        screen.blit(self.maxminheadlinelable, (10,5))
        screen.blit(self.outdoortemplable, (10,40))
        screen.blit(self.outdoortempvalues,(150,40))
        screen.blit(self.indoortemplable, (10, 75))
        screen.blit(self.indoortempvalues,(150,75))
        screen.blit(self.fridgetemplable, (10,110))
        screen.blit(self.fridgetempvalues,(150,110))
        screen.blit(self.freezertemplable, (10,145))
        screen.blit(self.freezertempvalues,(150,145))
        self.maxminstatebutton.draw(screen)

        return screen