__author__ = 'teddycool'
import urllib2
from WeatherStationConfig import config


class Server(object):
    def __init__(self):
        return

    def push(self, sensors):
        print "Pushing values to server"
        fullurl = config['Server']['url'] + sensors.urlString()
        fullurl=fullurl.replace(' ','%20')
        print fullurl
        try:
            #TODO: Handle users and som basic security
            urllib2.urlopen(fullurl)
        except:
            #TODO: handle buffering of calls and cache if they not succed
            pass