__author__ = 'teddycool'

import os, sys, pygame
from pygame.locals import *
import time
import MainLoop
from WeatherStationConfig import config
#import RPi.GPIO as GPIO
class Main(object):

    def __init__(self):
        # Init framebuffer/touchscreen environment variables for raspberry
       # if  os.sys.platform != 'win32':
           # GPIO.setmode(GPIO.BCM)
           # GPIO.setup(18,GPIO.OUT)
            #GPIO.output(18, False)
            #self._lightcontrolPwm =  GPIO.PWM(18, 50) #Pin 18 for backlight control and using default 50 hz
            #self._lightcontrolPwm.ChangeDutyCycle(20)
        print "Starting touchscreen"
        os.putenv('SDL_VIDEODRIVER', 'fbcon')
        os.putenv('SDL_FBDEV'      , '/dev/fb1')
        os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
        os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')
        print "Init pygame..."
        pygame.init()
        pygame.mouse.set_visible(False)
        print "Init Main object..."
        self._mainLoop=MainLoop.MainLoop()
        print "Setup screen"
        self.screen = pygame.display.set_mode((320,240))
        self._lastScreenUpdate = 0


    def run(self):
        print "Start run-loop..."


        self._mainLoop.initialize()
        stopped = False
        try:
            while not stopped:
                pos = (0,0)
                #TODO: add  keyboard catch for abort, ctrl-c
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if(event.type is MOUSEBUTTONDOWN):
                        pos = pygame.mouse.get_pos()
                #TODO: handle backlight and screen timeout
                self._mainLoop.update(self.screen, pos)
                self._mainLoop.draw(self.screen)
                pygame.display.flip()
                #TODO: set framerate based on time for each frame
                while time.time() - self._lastScreenUpdate < config["UpdateInterval"]["Screen"]:
                    time.sleep(0.01)
                self._lastScreenUpdate = time.time()
        finally:
            return
            #self._lightcontrolPwm.ChangeDutyCycle(100)
            #self._lightcontrolPwm.stop()
            #GPIO.cleanup()

#Testcode to run module. Standard Python way of testing modules.

if __name__ == "__main__":

    weatherstationloop=Main()
    weatherstationloop.run()
