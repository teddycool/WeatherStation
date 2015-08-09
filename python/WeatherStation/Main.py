__author__ = 'teddycool'

import os, sys, pygame
import time
import MainLoop


class Main(object):

    def __init__(self):
        # Init framebuffer/touchscreen environment variables for raspberry
        if  os.sys.platform != 'win32':
            os.putenv('SDL_VIDEODRIVER', 'fbcon')
            os.putenv('SDL_FBDEV'      , '/dev/fb1')
            os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
            os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')
        pygame.init()
        pygame.mouse.set_visible(False)
        print "Init Main object..."
        #Size of application window
        self.dwidth = 320
        self.dheight = 240
        self._mainLoop=MainLoop.MainLoop()


    def run(self):
        #Init and set up variables...
        print "Init pygame..."

        print "Setup screen"
        self.screen = pygame.display.set_mode((self.dwidth,self.dheight))
        self._mainLoop.initialize()
        self.size=(self.dwidth, self.dheight)

        black = 0, 0, 0
        #Init gamestate
        stopped = False
        running=True
        while not stopped:
            #TODO: add  keyboard catch for abort, ctrl-c
            black=0,0,0
            self.screen.fill(black)
            self._mainLoop.update(self.screen)
            self._mainLoop.draw(self.screen)
            pygame.display.flip()
            #TODO: set framerate based on time for each frame
            time.sleep(0.1)



#Testcode to run module. Standard Python way of testing modules.

if __name__ == "__main__":

    weatherstationloop=Main()
    weatherstationloop.run()
