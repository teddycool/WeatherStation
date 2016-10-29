<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//Retrieve current data and return it as simple xml, to use on website or android app etc
require_once('config.php');
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
if (mysqli_connect_error()) {
   echo "Connect failed: ".mysqli_connect_error()."<br>";
   exit();
}
$query = <<< EOD
SELECT outdoortemp, measuretime FROM `ws_data_shortterm` 
    WHERE outdoortemp is not NULL and servertime < (NOW() - INTERVAL 10 MINUTE) order by measuretime DESC limit 1
EOD;
// Perform the query
$res = $mysqli->query($query)
                        or die("Could not query database = \n {$query}");

$outdoortemp='-';

while($row1 = $res->fetch_object()) {
    $outdoortemp   = $row1->outdoortemp;
}

echo $outdoortemp;
?>