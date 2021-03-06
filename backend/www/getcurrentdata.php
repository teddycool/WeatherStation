<?php
//Retrieve current data and return it as simple xml, to use on website or android app etc
require_once('config.php');
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
if (mysqli_connect_error()) {
   echo "Connect failed: ".mysqli_connect_error()."<br>";
   exit();
}
$query = <<< EOD
SELECT * FROM `ws_data_shortterm` WHERE fridgetemphigh is not NULL order by measuretime DESC limit 1
EOD;
// Perform the query
$res = $mysqli->query($query)
                        or die("Could not query database = \n {$query}");


//TODO: add ir and alight variables..
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
    $irlight       = $row1->irlight;
    $amblight     = $row1->amblight;
}
$currentdata =<<<EOD
<?xml version="1.0" encoding="iso-8859-1"?>
<measures time = "{$time}" >
EOD;
$currentdata .= "<measure>";
$currentdata .= "<fridgetemplow> {$fridgetemplow} </fridgetemplow>";
$currentdata .= "<fridgetemphigh> {$fridgetemphigh} </fridgetemphigh>";
$currentdata .= "<freezertemp> {$freezertemp} </freezertemp>";
$currentdata .= "<outdoortemp> {$outdoortemp} </outdoortemp>";
$currentdata .= "<outdoorhum> {$outdoorhum} </outdoorhum>";
$currentdata .= "<outdoorbar> {$outdoorbar} </outdoorbar>";
$currentdata .= "<indoortemp> {$indoortemp} </indoortemp>";
$currentdata .= "<indoorhum> {$indoorhum} </indoorhum>";
$currentdata .= "<irlight> {$irlight} </iirlight>";
$currentdata .= "<amblight> {$amblight} </amblight>";
$currentdata .= "</measure>";
$currentdata .= "</measures>";
echo $currentdata;
