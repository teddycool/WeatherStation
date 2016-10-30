<?php
//Retrieves latest valid data for all columns
//Return it as simple xml, to use on website or android app etc
/*
 * XML-struct...
 * <?xml version="1.0" encoding="iso-8859-1"?>
*  <server time = '' >
 * <measures>
 *      <measure> name='' value='' time='' </value>  //For each column... 
 * </measures>
 */

require_once('config.php');
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
if (mysqli_connect_error()) {
   echo "Connect failed: ".mysqli_connect_error()."<br>";
   exit();
}

$servertime = date("Y-m-d H:i:s");

$currentdata =<<<EOD
<?xml version="1.0" encoding="iso-8859-1"?>
<server time = "{$servertime}" >
<measures>
EOD;

//First get all columns...
$cquery = <<< EOD
SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='yobnhr6641_ws1' 
    AND `TABLE_NAME`='ws_data_shortterm'
EOD;
$cres = $mysqli->query($cquery) or die("Could not query database = \n {$cquery}");

//For each column get latest value where not NULL together with measuringtime and add it to xml-data
$testarray = array('id', 'measuretime', 'servertime'); //Skip these columns...
while($col1 = $cres->fetch_object()) {
$column= $col1->COLUMN_NAME;
if (!in_array($column, $testarray))
{
//Get data for column...
$query = <<< EOD
SELECT {$column}, measuretime FROM `ws_data_shortterm` WHERE {$column} is not NULL order by measuretime DESC limit 1
EOD;
$res = $mysqli->query($query) or die("Could not query database = \n {$query}");
while($row1 = $res->fetch_object()) {
    $mtime= $row1->measuretime;  
    $value= $row1->{$column};
    //Add to xml...
    $currentdata .="<measure> name='{$column}' value='{$value}' time='{$mtime}' </value>";
}
}
}
$currentdata .= "</measures>";   
echo $currentdata;
?>