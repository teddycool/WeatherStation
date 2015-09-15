__author__ = 'teddycool'
import pygame
from WeatherStationConfig import config
import time

class StateLoopBase(object):
    def __init__(self):
        #same font everywhere
        self.myLargeFont = pygame.font.SysFont("Comic", 100)
        self.myNormalFont = pygame.font.SysFont("Comic", 25)
        self.myMediumFont = pygame.font.SysFont("Comic", 15)
        self.mySmallFont = pygame.font.SysFont("Comic", 10)
        self.myScaleFont = pygame.font.SysFont("Comic", 15)
        self.myButtonFont = pygame.font.SysFont("Comic", 10)
        self.stateButtons = []
        self._last_active = time.time()

    def initialize(self):
        return

    def update(self, mousepressedpos):
        #update states, return new state if changed

         return

    def draw(self, screen, sensors):
        testlable = self.myNormalFont.render("Inne:", 1, (0,255,0))
        screen.blit(testlable, (120, 100))
        return screen

    def init_sensors(self):
        #init all sensors
        self.indoortemp = 20
        return

    def update_sensors(self):
        #update stateloopvalues
        return

    def createTrendList(self, valuelist):
         if len(valuelist) < 5:
            return []
         newlist = []
        #Space on screen for last 150 values...
         if len(valuelist) > 150:
            newlist = list(valuelist[-150:])
         else:
            newlist = list(valuelist)
         step = 10
         newlist.reverse() #draw backwards 'now' is at the right end of trendline

         return newlist

    def drawTrend(self,screen, trendlist, ymin, ymax, color):

        maxvalue = max(trendlist)
        minvalue = min(trendlist)
        if maxvalue-minvalue == 0:
            maxvalue = round(1.1*maxvalue, 1)
            minvalue = round(0.9*minvalue, 1)
        ystep = (ymax-ymin)/abs(maxvalue-minvalue)
        maxstr =  self.myScaleFont.render(str(maxvalue), 1, config["Colors"]["Lables"])
        minstr =  self.myScaleFont.render(str(minvalue), 1, config["Colors"]["Lables"])

        prevalue = None
        thisvalue  = None
        linex = 310
        for value in trendlist:
            prevalue = thisvalue
            thisvalue = value
            if(prevalue != None and thisvalue != None):
                pygame.draw.line(screen, color, (linex,ymax-(prevalue-minvalue)*ystep), (linex-2,ymax-(thisvalue-minvalue)*ystep), 1)
                linex=linex-2
        screen.blit(maxstr, (290,ymin-10))
        screen.blit(minstr, (290,ymax-10))