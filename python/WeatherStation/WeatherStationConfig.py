__author__ = 'teddycool'
#Config values for WeatherStation.

config = {'UpdateInterval': {'Screen': 0.1, 'Server': 3600}, #times in seconds
          'MaxSavedValues': 1440, #24 hours
          'Server': {'url': 'full url to server script', 'user': 'username', 'password': 'userspassword', 'WSname': 'Name your station', 'WSId': 0},
          'RangeSensor':{'used': True, 'triggerpin': 23, 'echopin' : 24, 'activationdistance': 1}, #activationdistance in meters
          'DS18B20':{},
          'HumiditySensor': {},
          'Barometer': {},
          'Texts': {"outdoor": "Ute", "indoor": "Inne", "maxmin":"MaxMin", "cancel":"Avbryt", "currentstatehl":"Aktuella temperaturer",
                    "maxminstatehl":"Max//Min senaste 24 h"},
          'Colors': {"Lables": (255,255,255), "Values": (0,255,255), "Alarm": (255,0,0)}
            }

