<?php
    $name = "K";
    $age = "25";

    echo "Hello World!\n";
    echo 'The name is '.$name.' and the age is '.$age;
    
    $name = "L";
    define('NAME', 'KL');
    
    echo 'Changing name var to '.$name.' and the age to '.($age - 1);
    echo 'Const name is '.NAME;
?>