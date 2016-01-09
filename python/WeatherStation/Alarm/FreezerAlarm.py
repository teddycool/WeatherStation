
import time
from Inputs import IoInputs
from Actuators import LedIndicator
from Actuators import Buzzer

class FreezerAlarm(object):

    def __init__(self, GPIO, buzzer, button,):
        self._alarmstate = False
        return


    def initialize(self):
        return

    def update(self, freezersensordata):
        print "Frezzersensordata = " + str(freezersensordata)
        if not self._alarmstate:
            if self._hushBtn.update() == "LongPressed":
                #Start buzzer for test
                return
        else:
            if self._hushBtn.update() == "Pressed":
                #Stop buzzer sound
                return


        return


if __name__ == '__main__':
    print "Testcode for "