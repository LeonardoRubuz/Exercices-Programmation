
<?php
class Personne {
    public $taille;
    public $poids;
    public $age;

    public function __construct($taille, $poids, $age) {
        $this->taille = $taille;
        $this->poids = $poids;
        $this->age = $age;
    }
    

    public function imc() {
        return $this->poids / pow($this->taille, 2);
    }

    public function interpretation() {
        $imc = $this->imc();
        if ($imc <= 18.5) {
            echo "Insuffisance pondérale";
        } elseif ($imc >= 30) {
            echo "Obésité";
        }
    }
}
?>