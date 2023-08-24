<?php
function prix($n) {
  // Si n est inférieur ou égal à 20, le prix est de 10 centimes par copie
  if ($n <= 20) {
    return $n * 0.1;
  }
  // Sinon, le prix est de 10 centimes pour les 20 premières copies et de 8 centimes pour les suivantes
  else {
    return 20 * 0.1 + ($n - 20) * 0.08;
  }
}

// Tester la fonction avec les exemples donnés
echo prix(15); // Affiche 1.5
echo "\n";
echo prix(30); // Affiche 2.8
?>
