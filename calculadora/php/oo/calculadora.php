<?php

require_once "configs.php";

$firstOperation = new Calculator();
// set your first number below //
$firstOperation-> setNumber1(10);
// set your second number below //
$firstOperation-> setNumber2(5);
// set what is the operator | Addition -> + ; Subtration -> - ; Multiplication -> * ; Division -> / |
$firstOperation-> setOperator("+");
// this line code below will show the results //
echo $firstOperation-> verifyOperator();

?>