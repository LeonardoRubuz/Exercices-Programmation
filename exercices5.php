<?php
function aire_cercle($d) {
  $A = pi() * $d * $d / 4;
  return $A;
}

echo "L'aire d'un cercle de diamètre 10 cm est " . aire_cercle(10) . " cm²\n";
?>
