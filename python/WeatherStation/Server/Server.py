__author__ = 'teddycool'
import urllib2
import os
from WeatherStationConfig import config
import time


class Server(object):
    def __init__(self):
        self._urlcache=[]

    def push(self, sensors):
        print "Pushing sensorvalues to server"
        fullurl = config['Server']['url'] + sensors.urlString()
        fullurl=fullurl.replace(' ','%20')
        print fullurl
        #print "DEBUG... No sending of data"
        if  os.sys.platform != 'win32':
            self._urlcache.append(fullurl)
            try:
                for url in self._urlcache:
                    urllib2.urlopen(url)
                    time.sleep(0.1)
                self._urlcache = []
                print "Data sucessfully sent to server! URL-cache is empty"
            except:
                #TODO: handle buffering of calls and cache if they not succeeded
                print "Data sending aborted! URL-cache is not empty."
                pass