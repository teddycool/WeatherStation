__author__ = 'teddycool'
#State-switching and handling of general rendering
import pygame
import time
import sys
from Inputs import IoInputs
from Actuators import LedIndicator
from Actuators import Buzzer
from Sensors import Sensors
from WeatherStationConfig import config
from Server import Server
from Alarm import FreezerAlarm
import RPi.GPIO as GPIO


class MainLoop(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self._hushBtn = IoInputs.PushButton(GPIO, 26)
        self._alarmLed = LedIndicator.LedIndicator(GPIO, 16)
        self._sensorLed = LedIndicator.LedIndicator(GPIO, 12)
        self._alarmBuzzer = Buzzer.Buzzer(GPIO,5)
        self._sensors=Sensors.Sensors(GPIO)
        self._server = Server.Server()
        #self._freezerAlarm = FreezerAlarm.FreezerAlarm(GPIO)
        self._lastSensorUpdate = 0
        self._lastServerPush = 0
        return

    def initialize(self):
        print "Main init..."
        self.time=time.time()
        self._sensors.initialize()
        self._hushBtn.initialize()

        print "Station started at ", self.time

    def update(self):
        print "MainLoop update... " + time.strftime("%Y-%m-%d %H:%M:%S")
        self._sensorLed.update()
        self._alarmBuzzer.update()
        hushbtn = self._hushBtn.update()
        print "Hushbutton: " + hushbtn
        if hushbtn == 'LongPressed':
            self._alarmBuzzer.setState('test')
        #if hushbtn == 'Pressed':
        #    self._alarmBuzzer.setState('hush')

        if time.time() - self._lastSensorUpdate > config["UpdateInterval"]["Sensors"]:
            self._lastSensorUpdate = time.time()
            self._sensorLed.activate(True)
            self._sensors.update()
            self._server.push(self._sensors, 'short')
            print "Sensor values: " + self._sensors.toString()
            #self._freezerAlarm.update(self._sensors.sensorvaluesdict["FreezerTemp"]) #{current, trendlist}

            if time.time() - self._lastServerPush > config["UpdateInterval"]["Server"]:
                self._server.push(self._sensors, 'long')
                self._lastServerPush = time.time()
