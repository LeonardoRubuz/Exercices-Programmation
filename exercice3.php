<?php 

function truc($x){
    echo ($x);
    return $x*2;
    echo ($x*3);
    return $x*2;
}
truc(10); #la fonction truc renvoie 10 ça ne prend qu' en compte la fonction echo qui vient avant return


function bidule($x){
    echo ($x);
    echo ($x*2);
    return $x*3;
    echo ($x*4);

}
bidule(10); #la fonction bidule renvoie 10 et 20  ça ne prend qu' en compte les fonctions echo qui viennent  avant return
 


?>