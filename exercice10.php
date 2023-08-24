<?php
for ($i = 0; $i < 3; $i++) {
    echo "bidule";
}
echo "truc"; /* ce premier script renvoie budule trois fois avant d avoir truc à la fin*/

for ($i = 0; $i < 3; $i++) {
    echo "bidule";           /* pour le deuxieme script la premiere boucle renvoie bidule trois fois
                                et la deuxieme boucle renvoie truc quatre fois*/
}
for ($j = 0; $j < 4; $j++) {
    echo "truc";
}

?>