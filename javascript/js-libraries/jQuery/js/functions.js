$(function(){

    //fadeIn and fadeOut functions
    /*
    $('.box1').fadeOut(2000,function(){
        $('.box2').fadeIn(3000,function(){
            console.log('Animation finished');
        });
    });
    */

    //slideToggle function
    /*
    $('.box1').click(function(){
        $('.box2').slideToggle(2000,function(){
            location.href="http://www.google.com/";
        });
    });
    */


    //TimeOut function
    /*
    var timer;
    var timeOut = function(){
        $('.box2').animate({
            'width':'40%',
            'height':'500px',
            'marginLeft':'100px',
            'paddingTop':'200px'
        },2000);
    }

    $('body').click(function(){
        alert('Animation with timeout cancelled');
        clearTimeout(timer);
    });

    $('.box1').animate({
        'width':'40%',
        'height':'500px',
        'marginLeft':'100px',
        'paddingTop':'200px'
    },2000,function(){
        timer = setTimeout(timeOut,2000);
        //console.log('Animation finished');
    });
    */

    var timer;

    $('body').click(function(){
        alert('Animation with interval cancelled');
        clearInterval(timer);
    });

    timer = setInterval(function(){
        alert('hello world');
    },2000);
});