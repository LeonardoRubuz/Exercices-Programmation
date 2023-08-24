<?php
// Définir une fonction triangle qui renvoie la valeur du nombre triangulaire d'indice n
function triangle($n) {
  // Initialiser la somme à 0
  $sum = 0;
  // Faire une boucle de 1 à n
  for ($i = 1; $i <= $n; $i++) {
    // Ajouter i à la somme
    $sum += $i;
  }
  // Renvoyer la somme
  return $sum;
}

// Définir une fonction nbre_diviseurs qui renvoie le nombre de diviseurs d'un entier n
function nbre_diviseurs($n) {
  // Initialiser le compteur à 0
  $count = 0;
  // Faire une boucle de 1 à n
  for ($i = 1; $i <= $n; $i++) {
    // Si i divise n, incrémenter le compteur
    if ($n % $i == 0) {
      $count++;
    }
  }
  // Renvoyer le compteur
  return $count;
}

// Écrire un script qui détermine le plus petit nombre triangulaire qui admette au moins 50 diviseurs
// Initialiser l'indice à 1
$index = 1;
// Faire une boucle tant que le nombre de diviseurs du nombre triangulaire est inférieur à 50
while (nbre_diviseurs(triangle($index)) < 50) {
  // Augmenter l'indice de 1
  $index++;
}
// Afficher le nombre triangulaire et son indice
echo "Le plus petit nombre triangulaire qui admette au moins 50 diviseurs est " . triangle($index) . " et son indice est " . $index . "\n";

// Définir une fonction factorielle qui prend en argument un entier naturel n et renvoie n!
function factorielle($n) {
  // Si n est égal à 0 ou à 1, renvoyer 1
  if ($n == 0 || $n == 1) {
    return 1;
  }
  // Sinon, renvoyer n * factorielle(n-1)
  else {
    return $n * factorielle($n - 1);
  }
}

echo "64! = " . factorielle(64) . "\n";
?>
