__author__ = 'teddycool'
import sys
from Main import Main
weatherstationloop=Main()
try:
    weatherstationloop.run()
except:
    e = sys.exc_info()
    f = file("\home\pi\WeatherStation\exclog.log",'w')
    for l in e:
        f.write(str(l))



#Put in  /etc/rc.local for autostart at boot:
#cd /home/pi/WeatherStation
#sudo python weatherstart.py &
