<?php
function somme_cubes_chiffres($n) {
    $somme = 0;
    while ($n > 0) {
        $reste= $n % 10;
        $somme += pow($reste, 3);
        $n = floor($n / 10);
    }
     return $somme;
}
 echo somme_cubes_chiffres(256);

?>