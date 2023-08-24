<?php
function factorielle($n1) 
    { 
        $f1;
        $f3;
       if($n1 === 0)
          return 1;  
      else 
          return $n1*factorielle($n1-1); 
    }


          function facto($n2) 
    { 
        $f2;
       if($n2 === 0)
          return 1;  
      else 
          return $n2*factorielle($n2-1); 
    } 
     
    $n1=6;
    $f1 = factorielle($n1);
    echo("le factoriel de $n1 est $f1");
    echo(" ");

    $n2=4;  
    $f2=facto($n2); 
    echo("le factoriel de $n2 est $f2");
    echo(" ");

    $f3=$f1/$f2;
    echo("le quotient de $f1 sur $f2 est $f3");


    

?>