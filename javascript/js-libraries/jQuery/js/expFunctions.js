/*

$(document).ready(function(){
    alert("Hello World");
})

$(function(){
    alert("Hello World");
})

executam quando o documento terminar de carregar, mas pode ser que as imagens demorem a abrir

$(window).on('load', function(){
    alert("Hello World");
})

executa funcao somente quando o documento estiver carregado tudo totalmente

*/

/*
$(function(){
    $('.artigo1 > p').css('color', 'rgba(0,0,0,0,0.6)');
})
*/ 

/*
$(function(){
    function validateClickAndHover(){
        $('.article1').click(function(){
            $('.article2').css('background-color', 'purple');
        });

        $('.article1').hover(function(){
            $('.article2').css('background-color', 'red');
        }, function(){
            $('.article2').css('background-color', 'white');
        });
    }

    function validateFocusAndBlur(){
        $('.textarea').focus(function(){
            //Execute some function when there`s focus in the element.
            console.log('Inside textarea');
        }).blur(function(){
            //Execute some function when there`s no focus in the element.
            console.log('Outside textarea');
        });
    }

    function validateForm(){
        $('select').change(function(){
            console.log('Changed selected');
        });
    }

    validateClickAndHover();
    validateFocusAndBlur();
    validateForm();
});

*/
/*
$(function(){
    var timer;
    $(window).scroll (function(){
        //Scroll happens event
    })

    $(window).resize(function(){
        //resize screen event
        //console.log("Screen resizing");
        clearTimeout(timer);
        timer = setTimeout(function(){
            location.href = "http://127.0.0.1:5500/index.html";
        },1000);

        $('a').click(function(e){
            //e.preventDefault();

           //return false;
           
        })
    })
})
*/

/*
$(function(){
    $('body').click(function(){
        $('.box').css('background-color', 'green');
    });

    $('.box').click(function(e){
        e.stopPropagation();
    })
});
*/
/*
$(function(){
    var el = $('div.box');

    el.css('background-color','aqua');

    function test(){
        el.css('color','white');
    };

    test();
})
*/

$(function(){
    //take the element width
    $('.box').width();

    //Set width
    $('.box').css('width','900px')
    $('.box').css('height','700px')
    //Width/height = total dimension based on padding
    //InnerWidth/height = total dimension including padding
    //OuterWidth/height = total dimension including padding and margin (if parameter is true)

    console.log("Width:"+$('.box').width());
    console.log("InnerWidth:"+$('.box').innerWidth());
    console.log("OuterWidth:"+$('.box').outerWidth(true));

    console.log("Height:"+$('.box').width());
    console.log("InnerHeight:"+$('.box').innerWidth());
    console.log("OuterHeight:"+$('.box').outerWidth(true));
});