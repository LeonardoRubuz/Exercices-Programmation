<?php
    if (isset($_POST['n'])) {
        $n = $_POST['n'];
        $racine = sqrt($n);
        if ($racine == floor($racine)) {
            echo "Le nombre $n est un carré parfait.";
        } else {
            echo "Le nombre $n n'est pas un carré parfait.";
        }
    
    }else{
  ?>  <form method="post">
        Entrez un nombre entier: <input type="text" name="n">
        <input type="submit" value="Envoyer">
    </form>
    <?php
    }
    
    ?>






