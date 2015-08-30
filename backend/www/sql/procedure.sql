CREATE PROCEDURE `insertWeatherData`

( IN `ameasuretime` DATETIME, IN `afridgetemphigh` FLOAT, IN `afridgetemplow` FLOAT,
IN `afreezertemp` FLOAT, IN `aoutdoortemp` FLOAT, 
IN `aindoortemp` FLOAT, IN `aoutdoorhum` FLOAT, IN `aindoorhum` FLOAT, 
IN `aoutdoorbar` FLOAT)
BEGIN
INSERT INTO ws_data (servertime, measuretime, fridgetemphigh, fridgetemplow,freezertemp, outdoortemp, indoortemp, outdoorhum,indoorhum, outdoorbar) 
VALUES (NOW(), ameasuretime, afridgetemphigh, afridgetemplow, afreezertemp, aoutdoortemp, aindoortemp,aoutdoorhum, aindoorhum,aoutdoorbar)
END












  
  `indoortemp` float NOT NULL,
  `outdoorhum` float NOT NULL,
  `indoorhum` float NOT NULL,
  `outdoorbar` float NOT NULL
