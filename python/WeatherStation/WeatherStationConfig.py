__author__ = 'teddycool'
#Config values for WeatherStation.

config = {'UpdateInterval': {'Sensors': 60, 'Server': 600, 'Screen': 0, "Saver": 10}, #times in seconds
          'MaxSavedValues': 1440,
          'Server': {'url': 'http://www.sundback.com/ws/weatherdataupload.php', 'user': 'username', 'password': 'userspassword', 'WSname': 'Name your station', 'WSId': 0},
          'Colors': {"Lables": (255,255,255), "Values": (0,255,255), "Alarm": (255,0,0), "SaverText": (80,80,80)},
          'Logging':{'Log':True, "Logfile":"weatherlog.log", "PushToServer": True}
            }

