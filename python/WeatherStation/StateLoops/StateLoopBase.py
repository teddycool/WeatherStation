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

    def prepareTrendList(self, valuelist):
        #TODO: calculate interval for picking values from list. List is last 24h X-stepping is 2 and there is place for 150 values with standardsetting every 10th
        step = 10
        trendlist = []
        index=0
        while len(trendlist) < 150:
            try:
                trendlist.append(valuelist[index])
                index=index+step
            except:
                break
        trendlist.reverse() #draw backwards 'now' is at the right end of trendline
        return trendlist

    def drawTrend(self,screen, trendlist, ymin, ykoff, yoffset, color):

        #TODO: calculate offset/scaling for values depending on max/min in list and given ymin/ymax
        prevalue = thisvalue  = None
        linex = 310
        for value in trendlist:
            prevalue = thisvalue
            thisvalue = value
            if(prevalue != None and thisvalue != None):
                pygame.draw.line(screen, color, (linex,ymin+(prevalue-yoffset)*ykoff), (linex-2,ymin+(thisvalue-yoffset)*ykoff), 1)
                linex=linex-2