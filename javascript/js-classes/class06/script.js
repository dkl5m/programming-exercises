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

    // Calling game function at each 100 ms
    setInterval(game, 100)
}

function game(){
    // Screen config
    context.fillstyle = "#2980B9"
    // distance h border, distance v border, width, height
    context.fillRect(0, 0, canvas.width, canvas.height)

    // Moving the snake
    snake.push({x: positionX, y: positionY})
    console.log(snake[0])

    // snake config
    context.fillstyle = "00f102"
    for(let i = 0; i < snake.length; i++){
        context.fillRect(snake[i].x*grid, snake[i].y*grid, grid - 1, grid -1)
    }

}