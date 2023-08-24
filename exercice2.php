<?php

$nbr_photocopie1=15;
$nbr_photocopie2=30;
$prix1=$nbr_photocopie1*10;
$prix2=20*10 +(30-20)*8;
echo sprintf(" le prix1 est %d centimes",$prix1);
echo sprintf(" le prix2 est %d centimes",$prix2);

function prix($nbr_photocopie){

    if($nbr_photocopie<=20){

        return $nbr_photocopie*0.10 ;      
    }else{
    
        return 20*10+($nbr_photocopie-20)*0.08;
        
    } 
    
}
   echo prix(15);

?>
