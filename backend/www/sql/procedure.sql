

CREATE DEFINER=`yobnhr6641`@`localhost` PROCEDURE `insertWeatherDataLt`
( IN `ameasuretime` DATETIME, IN `afridgetemphigh` FLOAT, IN `afridgetemplow` FLOAT,
IN `afreezertemp` FLOAT, IN `aoutdoortemp` FLOAT, 
IN `aindoortemp` FLOAT, IN `aoutdoorhum` FLOAT, IN `aindoorhum` FLOAT, 
IN `aoutdoorbar` FLOAT, IN `airlight` FLOAT, IN `aamblight` FLOAT)
INSERT INTO ws_data_longterm (servertime, measuretime, fridgetemphigh, fridgetemplow,freezertemp, outdoortemp, indoortemp, outdoorhum,indoorhum, outdoorbar, irlight, amblight ) 
VALUES (NOW(), ameasuretime, afridgetemphigh, afridgetemplow, afreezertemp, aoutdoortemp, aindoortemp,aoutdoorhum, aindoorhum,aoutdoorbar, airlight, aamblight )



CREATE DEFINER=`yobnhr6641`@`localhost` PROCEDURE `insertWeatherDataSt`( IN `ameasuretime` DATETIME, IN `afridgetemphigh` FLOAT, IN `afridgetemplow` FLOAT,
IN `afreezertemp` FLOAT, IN `aoutdoortemp` FLOAT, 
IN `aindoortemp` FLOAT, IN `aoutdoorhum` FLOAT, IN `aindoorhum` FLOAT, 
IN `aoutdoorbar` FLOAT, IN `airlight` FLOAT, IN `aamblight` FLOAT)
INSERT INTO ws_data_shortterm (servertime, measuretime, fridgetemphigh, fridgetemplow,freezertemp, outdoortemp, indoortemp, outdoorhum,indoorhum, outdoorbar, irlight, amblight ) 
VALUES (NOW(), ameasuretime, afridgetemphigh, afridgetemplow, afreezertemp, aoutdoortemp, aindoortemp,aoutdoorhum, aindoorhum,aoutdoorbar, airlight, aamblight )



