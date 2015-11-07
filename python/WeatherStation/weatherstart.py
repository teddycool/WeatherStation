__author__ = 'teddycool'

from Main import Main
weatherstationloop=Main()
weatherstationloop.run()



#Put in  /etc/rc.local for autostart at boot:
#cd /home/pi/WeatherStation
#sudo python weatherstart.py &
