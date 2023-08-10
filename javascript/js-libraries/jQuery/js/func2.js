$(function(){
    /* ex1
    //function append() add content to the final of the selected element.
    $('.box div').eq(1).append('<h3>My element added dinamically</h3>');

    var el = $('<h3>My content</h3>').appendTo($('.box')).css('color','blue');

    //function prepend() add content to the beginning of the selected element.
    $('.box').prepend('<h3>Hello World</h3>');
    
    var el1 = $('<h3>My content</h3>').prependTo($('.box')).css('color','red');
    */

    /* ex2
    var t = 'My content after div box';
    $('.box').after(t);
    $(t).insertAfter($('.box')).css('color', 'green');

    $('.box').before(t);
    $(t).insertBefore($('.box')).css('color', 'green');

    setTimeout(() => {
       $('.box').eq(1).remove(); 
    }, 3000);
    */
});