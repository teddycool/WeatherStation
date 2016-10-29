<?php

/* 
 * This is used to receive the weatherdata from the raspberry pi
 * The Query-string is unpacked and stored in db with a SQL-procedure
 * 
 */

error_reporting(E_ALL|E_STRICT);
require_once('config.php');
date_default_timezone_set("Europe/Berlin");
// ("%Y-%m-%d %H:%M:%S") 
$servertime = date("Y-m-d H:i:s");

//$servertime= ( "%Y-%m-%d %H:%M:%S",time());

// Get all variables.
$AllData = $_SERVER["QUERY_STRING"];

//weatherdata from query-string


$atable                     = isset($_GET['table']) ? $_GET['table'] : 'NULL';
$atimestamp             = isset($_GET['time']) ? $_GET['time'] : $servertime;
$afridgetemphigh        = isset($_GET['FridgeTempUpper']) ? $_GET['FridgeTempUpper'] : 'NULL';
$afridgetemplow         = isset($_GET['FridgeTempLower']) ? $_GET['FridgeTempLower'] : 'NULL';
$afreezertemp         = isset($_GET['FreezerTemp']) ? $_GET['FreezerTemp'] : 'NULL';
$aoutdoortemp           = isset($_GET['OutdoorTemp']) ? $_GET['OutdoorTemp'] : 'NULL';
$aindoortemp            = isset($_GET['IndoorTemp']) ? $_GET['IndoorTemp'] : 'NULL';
$aoutdoorhum            = isset($_GET['OutdoorHum']) ? $_GET['OutdoorHum'] : 'NULL';
$aindoorhum             = isset($_GET['IndoorHum']) ? $_GET['IndoorHum'] : 'NULL';
$aoutdoorbar            = isset($_GET['OutdoorBar']) ? $_GET['OutdoorBar'] : 'NULL';
$airlightlevel          = isset($_GET['IrLight']) ? $_GET['IrLight'] : 'NULL';
$aambilightlevel          = isset($_GET['ALight']) ? $_GET['ALight'] : 'NULL';

echo $servertime;

$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
if (mysqli_connect_error()) {
   echo "Connect failed: ".mysqli_connect_error()."<br>";
   exit();
}
$procedure = '';
if ($atable=='short'){
    $procedure = insertWeatherDataSt;    
}
else {
    if ($atable=='long'){
        $procedure = insertWeatherDataLt;  
    }
    else {
        die("No proper procedure selected");
    }
 }

$query = <<< EOD
CALL {$procedure}('{$atimestamp}',{$afridgetemphigh},{$afridgetemplow},{$afreezertemp},{$aoutdoortemp}, {$aindoortemp}, {$aoutdoorhum},{$aindoorhum}, {$aoutdoorbar}, {$airlightlevel}, {$aambilightlevel})
EOD;
// Perform the query
$res = $mysqli->query($query)
                        or die("Could not query database = \n {$query}");
 
//Adding data went well, now clean out old stuff from shortterm table. 
//TODO: Ugly direct call, should be moved to procedure with a variable for the interval                        
$query = "DELETE FROM ws_data_shortterm WHERE servertime < (NOW() - INTERVAL 24 HOUR)";
$res = $mysqli->query($query)
      or die("Could not query database = \n {$query}");                            
?>


    