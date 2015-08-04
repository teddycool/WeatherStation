__author__ = 'teddycool'

import os, sys, pygame

import MainLoop


class Main(object):

    def __init__(self):
        print "Init Main object..."
        #Size of application window
        self.dwidth = 320
        self.dheight = 240
        self._mainLoop=MainLoop.MainLoop()


    def run(self):
        #Init and set up variables...
        print "Init pygame..."
        pygame.init()
        print "Setup screen"
        self.screen = pygame.display.set_mode((self.dwidth,self.dheight))
        self._mainLoop.initialize()
        self.size=(self.dwidth, self.dheight)

        black = 0, 0, 0
        #Init gamestate
        stopped = False
        running=True
        while not stopped:
            black=0,0,0
            self.screen.fill(black)
            self._mainLoop.update(self.screen)
            self._mainLoop.draw(self.screen)
            pygame.display.flip()



#Testcode to run module. Standard Python way of testing modules.

if __name__ == "__main__":

    weatherstationloop=Main()
    weatherstationloop.run()
