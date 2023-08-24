<?php
if (isset($_POST['string'])) {
    $string = $_POST['string'];
    $position = strpos($string, 'a');
    if ($position !== false) {
        echo "La lettre  'a' est  $position.";
    } else {
        echo "La lettre 'a' n est pas trouvéé.";
    }
} else {
?>
<form method="post">
    Entrer une phrqse : <input type="text" name="string">
    <input type="submit" value="Submit">
</form>
<?php
}
?>