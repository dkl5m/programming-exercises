<?php
    /*
    $name = "K";
    $age = "25";

    echo "Hello World!\n";
    echo 'The name is '.$name.' and the age is '.$age;
    
    $name = "L";
    define('NAME', 'KL');
    
    echo 'Changing name var to '.$name.' and the age to '.($age - 1);
    echo '<h2>Const name is '.NAME.'</h2>';
    echo '<script>alert("Hello World");</scripts>';

    $students = array('Jack', 'Monica', 'Gojo');
    echo $students[1];
    $students2 = array('student' => 'Jack', 'Monica', 'Gojo');
    echo $students2['student'];

    foreach ($students as $key => $value){
        echo $value;
        echo '<br/>';
    }

    foreach ($students as $key => $value){
        echo $key;
        echo '<br/>';
    }

    for($i = 0; $i < 10; $i++){
        echo $i;
        echo '<br/>';
    }

    $stu = array('One', 'Mon', 'Hour');
    for($i = 0; $i < sizeof($stu); $i++){
        echo $i;
        echo '<br/>';
    }

    $i = 0;
    while($i < 10){
        echo 'Message'.$i;
        echo '<br/>';
        $i++;
    }
    */

    /*
    function sum($n1, $n2){
        // logic
        return $n1+$n2;
    }

    echo sum(10,20);

    function verifyName($name){
        if($name == 'Krinson'){
            return 2.5;
        }else{
            return false;
        }
    }

    if(verifyName('Krinson') == '2.5'){
        echo 'True';
    }

    function verifyName1($name = 'Krinson1'){
        echo $name;
    }

    verifyName1();
    */

    $phrase = 'Kal is a dev';
    //$newPhrase = str_replace('Kal', 'Tank', $phrase);
    //echo $newPhrase;

    //$newPhrase = substr($phrase,0,4);
    //echo $newPhrase;

    $newPhrase = explode(' ', $phrase);
    //print_r($newPhrase);

    $newPhrase = implode(' ', $newPhrase);
    echo $newPhrase;

?>