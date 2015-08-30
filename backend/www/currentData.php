<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$html = <<<EOD
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="iso-8859-1" />
        <title></title>
    </head>
EOD;
require_once('config.php');
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
if (mysqli_connect_error()) {
   echo "Connect failed: ".mysqli_connect_error()."<br>";
   exit();
}


$query = <<< EOD
SELECT * FROM `ws_data` order by measuretime DESC limit 1
EOD;
// Perform the query
$res = $mysqli->query($query)
                        or die("Could not query database = \n {$query}");

$main = "";
while($row1 = $res->fetch_object()) {
    $fridgetemphigh= $row1->fridgetemphigh;
    $fridgetemplow = $row1->fridgetemplow;
    $freezertemp   = $row1->freezertemp;
    $outdoortemp   = $row1->outdoortemp;
    $outdoorhum    = $row1->outdoorhum;
    $outdoorbar    = $row1->outdoorbar;
    $indoortemp    = $row1->indoortemp;
    $indoorhum     = $row1->indoorhum;
    $time          = $row1->measuretime;
    
    
    
}
$html .= "<h2>Senaste mätningen:</h2>";
$html .= "<br/>Tid:   {$time}<br/><br/>";
$html .= "Kylen: {$fridgetemplow}C, {$fridgetemphigh}C<br/>";
$html .= "Frysen: {$freezertemp}C<br/><br/>";
$html .= "Ute:  {$outdoortemp}C, {$outdoorhum}% {$outdoorbar}kPa<br/>";
$html .= "Inne: {$indoortemp}C, {$indoorhum}%";

print $html;
