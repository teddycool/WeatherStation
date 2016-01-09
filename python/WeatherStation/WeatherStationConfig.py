__author__ = 'teddycool'
#Config values for WeatherStation.
#Tactics: In this 'no-screen' project where data is shown on a external networked device the data has to be sent to the database at a more often cycle
#The database depends on two tables: short- and long-term.
#   Short-term is for the last 24 hours and contiune data for each sensor read as defined below.
#   Long-term is storing data at the interval for 'server' below
# When data is sent to the sql-server the insert procedure loads the short-term datatable, removes older stuff and also load the data to the long-term table
# if the last record is older then server inteval

config = {'UpdateInterval': {'Sensors': 10, 'Server': 60, }, #times in seconds
          'MaxSavedValues': 2880,  # for future local trend-calcultations and alarms
          'Server': {'url': 'http://www.sundback.com/ws/weatherdataupload2.php', 'user': 'username', 'password': 'userspassword', 'WSname': 'Name your station', 'WSId': 0},
          #'Logging':{'Log':True, "Logfile":"weatherlog.log", "PushToServer": True},
          'LedIndicator': {"ActivationTime": 2},
          "Button": {"Pressed": 0.5, "LongPressed": 3}, #times in seconds
          "Alarm": {"Freezer": -10}
            }

