<?php

$index = "";

$index = readline("Type an index:\n");

if ( $index <= 0 or $index >= 3200000 ) {
    echo "Please input a natural index from 1 to 3200000!";
    echo "\n";
    exit;
}

$sequence = "";
$number = 1;
while ( strlen($sequence) < $index ) {

    $sequence .= $number * $number;
    $number++;

}

print substr($sequence,$index-1,1);
echo "\n";

?>
