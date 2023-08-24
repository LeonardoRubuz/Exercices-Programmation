<?php

function diviseur($nbr){
    for($i=1; $i<= $nbr;$i++){
        if(($nbr% $i)==0){
            echo ($i);

            
        }
    }
}
echo diviseur(10);

?>
