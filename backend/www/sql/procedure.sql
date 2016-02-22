qCREATE PROCEDURE `insertWeatherDataLt`

( IN `ameasuretime` DATETIME, IN `afridgetemphigh` FLOAT, IN `afridgetemplow` FLOAT,
IN `afreezertemp` FLOAT, IN `aoutdoortemp` FLOAT, 
IN `aindoortemp` FLOAT, IN `aoutdoorhum` FLOAT, IN `aindoorhum` FLOAT, 
IN `aoutdoorbar` FLOAT, IN `airlight` FLOAT, IN `aamblight` FLOAT)
BEGIN
INSERT INTO ws_data_longterm (servertime, measuretime, fridgetemphigh, fridgetemplow,freezertemp, outdoortemp, indoortemp, outdoorhum,indoorhum, outdoorbar, irlight, amblight ) 
VALUES (NOW(), ameasuretime, afridgetemphigh, afridgetemplow, afreezertemp, aoutdoortemp, aindoortemp,aoutdoorhum, aindoorhum,aoutdoorbar, airlight, aamblight )

END


--- add light and ir
--- create a shortterm and a longterm table (rename current to longterm?)
--- fix procedure to maintain tables, remove old rows from shortterm and only add to longterm every x minute





CREATE DEFINER=`yobnhr6641`@`localhost` PROCEDURE `insertWeatherDataLt`
( IN `ameasuretime` DATETIME, IN `afridgetemphigh` FLOAT, IN `afridgetemplow` FLOAT,
IN `afreezertemp` FLOAT, IN `aoutdoortemp` FLOAT, 
IN `aindoortemp` FLOAT, IN `aoutdoorhum` FLOAT, IN `aindoorhum` FLOAT, 
IN `aoutdoorbar` FLOAT, IN `airlight` FLOAT, IN `aamblight` FLOAT)
INSERT INTO ws_data_longterm (servertime, measuretime, fridgetemphigh, fridgetemplow,freezertemp, outdoortemp, indoortemp, outdoorhum,indoorhum, outdoorbar, irlight, amblight ) 
VALUES (NOW(), ameasuretime, afridgetemphigh, afridgetemplow, afreezertemp, aoutdoortemp, aindoortemp,aoutdoorhum, aindoorhum,aoutdoorbar, airlight, aamblight )






  
  `indoortemp` float NOT NULL,
  `outdoorhum` float NOT NULL,
  `indoorhum` float NOT NULL,
  `outdoorbar` float NOT NULL
