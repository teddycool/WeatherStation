__author__ = 'teddycool'
import pygame
from StateLoopBase import StateLoopBase
from GuiComponents import Button
from WeatherStationConfig import config
import time

class CurrentValues(StateLoopBase):
    def __init__(self):
        super(CurrentValues, self).__init__()
        return

    def initialize(self, sensors):
        #Init buttons etc for MainLoop
        self.fridgeFreezerTrendBtn = Button.Button((20,210,50, 10))
        self.fridgeFreezerTrendBtn.color=(0,255,0)
        self.fridgeFreezerTrendBtn.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.fridgeFreezerTrendBtn.text= "KylFrys"
        self.outdoorTrendBtn = Button.Button((100,210,50, 10))
        self.outdoorTrendBtn.color=(0,255,0)
        self.outdoorTrendBtn.iconFg= pygame.image.load("icons/Frame_Down.png")
        self.outdoorTrendBtn.text= "Ute"
        self.trendLable =  self.myNormalFont.render("Visa trender:", 1, config["Colors"]["Lables"])
        self.outdoortemplable = self.myNormalFont.render("Ute:", 1, config["Colors"]["Lables"])
        self.indoortemplable = self.myNormalFont.render("Inne:", 1, config["Colors"]["Lables"])
        self.fridgetemplable = self.myNormalFont.render("Kylen:", 1, config["Colors"]["Lables"])
        self.freezertemplable = self.myNormalFont.render("Frysen:", 1, config["Colors"]["Lables"])

        self.indoortempvalues= self.myNormalFont.render(" -- ", 1, config["Colors"]["Values"])
        self.outdoortempvalues= self.myNormalFont.render(" -- ", 1, config["Colors"]["Values"])
        self.fridgetempvalues = self.myNormalFont.render(" -- ", 1, config["Colors"]["Values"])
        self.freezertempvalues = self.myNormalFont.render(" -- ", 1, config["Colors"]["Values"])
        self._last_active = time.time()
        return

    def update(self, mousepressedpos):
        if time.time()-self._last_active > config["UpdateInterval"]["Saver"]:
            return "SaverScreen"
        if self.fridgeFreezerTrendBtn.selected(mousepressedpos):
            return "FridgeFreezerTrend"
        if self.outdoorTrendBtn.selected(mousepressedpos):
            return "OutdoorTrend"
        else:
            return None

    def draw(self, screen, sensors):

        #Draw CurrentValues screen
        self.fridgetempvalues = self.myNormalFont.render(str(sensors.sensorvaluesdict["FridgeTempUpper"]["Current"]) + " C " + str(sensors.sensorvaluesdict["FridgeTempLower"]["Current"]) + " C", 1, config["Colors"]["Values"])
        self.indoortempvalues = self.myNormalFont.render(str(sensors.sensorvaluesdict["IndoorTemp"]["Current"]) + " C " + str(sensors.sensorvaluesdict["IndoorHum"]["Current"]) + " %", 1, config["Colors"]["Values"])
        self.outdoortempvalues = self.myNormalFont.render(str(sensors.sensorvaluesdict["OutdoorTemp"]["Current"]) + " C " + str(sensors.sensorvaluesdict["OutdoorHum"]["Current"]) + " % " +
                                                          str(sensors.sensorvaluesdict["OutdoorBar"]["Current"]) + " kPa", 1, config["Colors"]["Values"])

        self.freezertempvalues = self.myNormalFont.render(str(sensors.sensorvaluesdict["FreezerTemp"]["Current"]) + " C ", 1, config["Colors"]["Values"])
        #pygame.draw.rect(screen,(255,0,0),pygame.Rect(0, 0, 320, 240),5 )
        screen.blit(self.trendLable, (10,170))
        screen.blit(self.outdoortemplable, (10,40))
        screen.blit(self.outdoortempvalues,(100,40))
        screen.blit(self.indoortemplable, (10, 75))
        screen.blit(self.indoortempvalues,(100,75))
        screen.blit(self.fridgetemplable, (10,110))
        screen.blit(self.fridgetempvalues,(100,110))
        screen.blit(self.freezertemplable, (10,145))
        screen.blit(self.freezertempvalues,(100,145))
        self.fridgeFreezerTrendBtn.draw(screen)
        self.outdoorTrendBtn.draw((screen))

        return screen