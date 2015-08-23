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
        print "Init pygame..."
        pygame.init()
        pygame.mouse.set_visible(False)
        print "Init Main object..."
        self._mainLoop=MainLoop.MainLoop()
        print "Setup screen"
        self.screen = pygame.display.set_mode((320,240))


    def run(self):
        print "Start run-loop..."

        self._mainLoop.initialize()
        stopped = False
        while not stopped:
            #TODO: add  keyboard catch for abort, ctrl-c

            self._mainLoop.update(self.screen)
            self._mainLoop.draw(self.screen)
            pygame.display.flip()
            #TODO: set framerate based on time for each frame
            time.sleep(0.1)



#Testcode to run module. Standard Python way of testing modules.

if __name__ == "__main__":

    weatherstationloop=Main()
    weatherstationloop.run()
