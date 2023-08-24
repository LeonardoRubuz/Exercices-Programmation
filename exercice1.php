<?php
$temps=42569;
$heure=$temps/3600;
$reste=$temps % 3600;
$minute=$reste/60;
$seconde=$reste % 60;
echo sprintf("%d:%d:%d",$heure,$minute,$seconde);
?>

