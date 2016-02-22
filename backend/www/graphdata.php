<?php
require_once('config.php');
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
if (mysqli_connect_error()) {
   echo "Connect failed: ".mysqli_connect_error()."<br>";
   exit();
}


$return_arr = array();

$query = <<< EOD
SELECT * FROM `ws_data_shortterm` order by measuretime DESC limit 10
EOD;
// Perform the query
$res = $mysqli->query($query)
                        or die("Could not query database = \n {$query}");

                       
while($row = $res->fetch_object()) {
    $row_arr= array();
    $row_arr['measuretime'] = $row->measuretime;
    $row_arr['fridgetemphigh'] = $row->fridgetemphigh;
    $row_arr['fridgetemplow']  = $row->fridgetemplow; 
    $row_arr['freezertemp']  = $row->freezertemp; 
    $row_arr['outdoortemp']  = $row->outdoortemp;  
    $row_arr['outdoorhum']  = $row->outdoorhum;
    $row_arr['outdoorbar']  = $row->outdoorbar; 
    $row_arr['indoortemp']  = $row->indoortemp; 
    $row_arr['indoorhum']  = $row->indoorhum; 
    
    array_push($return_arr,$row_arr);
}
 
echo json_encode($return_arr);