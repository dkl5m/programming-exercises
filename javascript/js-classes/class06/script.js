window.onload = function(){
    canvas = document.getElementById("canvas");
    context = canvas.getContext("2d");

    // Vars
    snake = [];
    positionX = 10;
    positionY = 10;
    foodX = 15;
    foodY = 15;
    velX = 0;
    velY = 0;
    grid = 20;
    size = 3;
}