__author__ = 'teddycool'
import pygame

class StateLoop(object):
    def __init__(self):
        #same font everywhere
        self.myFont = pygame.font.SysFont("Arial", 25)

    def initialize(self):
        return

    def update(self, screen):
        #update all sensorvalues
        return screen

    def draw(self, screen, sensors):
        testlable = self.myFont.render("Inne:", 1, (0,255,0))
        screen.blit(testlable, (120, 100))
        return screen

    def init_sensors(self):
        #init all sensors
        self.indoortemp = 20
        return

    def update_sensors(self):
        #update all sensorvalues
        return