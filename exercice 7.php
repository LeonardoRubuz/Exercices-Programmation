<?php
// Définir une fonction somme_cubes_chiffres qui prend en argument un entier naturel et renvoie la somme des cubes de ses chiffres
function somme_cubes_chiffres($n) {
  $sum = 0;
  // Convertir l'entier en chaîne de caractères
  $str = strval($n);
  for ($i = 0; $i < strlen($str); $i++) {
    // Convertir le caractère en entier et calculer son cube
    $cube = intval($str[$i]) ** 3;
    // Ajouter le cube à la somme
    $sum += $cube;
  }
  return $sum;
}

for ($n = 0; $n < 10000; $n++) {
  // Si le nombre est égal à la somme des cubes de ses chiffres, c'est un nombre d'Armstrong
  if ($n == somme_cubes_chiffres($n)) {
    echo "$n est un nombre d'Armstrong car $n = " . somme_cubes_chiffres($n) . "\n";
  }
}
?>
