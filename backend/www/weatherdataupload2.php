<?php

/* 
 * This is used to receive the weatherdata from the raspberry pi
 * The Query-string is unpacked and stored in db with a SQL-procedure
 * 
 */

error_reporting(E_ALL|E_STRICT);
require_once('config.php');
date_default_timezone_set("Europe/Berlin");
$servertime = time();  //PHP time...

// Get all variables.
$AllData = $_SERVER["QUERY_STRING"];

//weatherdata from query-string


$atable             = isset($_GET['table']) ? $_GET['table'] : 'NULL';
$atimestamp             = isset($_GET['time']) ? $_GET['time'] : 'NULL';
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
}



$query = <<< EOD
CALL {$procedure}('{$atimestamp}',{$afridgetemphigh},{$afridgetemplow},{$afreezertemp},{$aoutdoortemp}, {$aindoortemp}, {$aoutdoorhum},{$aindoorhum}, {$aoutdoorbar}, {$airlightlevel}, {$aambilightlevel})
EOD;
// Perform the query
$res = $mysqli->query($query)
                        or die("Could not query database = \n {$query}");
                
?>


    