<?php
    class DankiCode
    {
        public $name = 'John';
        #Constructor method
        /*
        function __construct($name)
        {
            echo $name;
        }
        */

        public function printName(){
            return 'Khan';
        }
    }

    //Instancing a class
    $dankiCode = new DankiCode();

    //echo $dankiCode->printName();

    echo $dankiCode->name;
?>