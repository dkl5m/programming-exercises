$(function(){
  
    /*
    $('a').click(function(){
        alert('Hello World');
    });

    $('body').on('click','a',function(){
        alert('Hello World');
        return false;
    });

    setTimeout(function(){
        $('body').html('<a href="">My link</a>');
    },3000);
    */

    /*
    var func = function(){
        //$(this).css('background', 'blue');
        //console.log($(this).index()); //Show id
        //$('input[type=text]').eq($(this).index().css('background', 'blue'));
        var id = $(this).index();
        $('input[type=text]').eq(id).css('background', 'blue');
    }
    //$('input[name=namePerson]').keyup(func);
    $('input[type=text]').keyup(func); //When let the button
    $('input[type=text]').keydown(func); //When pressing the button
    */

    $('form.form-contact').submit(function(){
        //var input = $('.form-contact input[type=text]');

        var container = $('.container');
        var content = 'Name: ' + $('input[name=name]').val() +
        '<hr>E-mail: ' + $('input[name=email]').val() +
        '<hr>Phone: ' + $('input[name=phone]').val();

        container.html(content);
        return false;
    })
});