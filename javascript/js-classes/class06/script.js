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
    size = 2;

    // Calling game function at each 100 ms
    setInterval(game, 100)

    // Controls
    document.addEventListener(
        "keydown",
        (event) => {
            if (event.defaultPrevented) {
                return; // Do nothing if the event was already processed
            }

            switch (event.code) {
                case "ArrowDown":
                    velX=0;
                    velY=1;
                    break;
                case "ArrowUp":
                    velX=0;
                    velY=-1;
                    break;
                case "ArrowLeft":
                    velX=-1;
                    velY=0;
                    break;
                case "ArrowRight":
                    velX=1;
                    velY=0;
                    break;
                default:
                    return; // Quit when this doesn't handle the key event.
            }
        // Cancel the default action to avoid it being handled twice
        event.preventDefault();
        },
        true,
    );
}

function game(){
    // Screen config
    context.fillStyle = "#86ebff"
    // Distance h border, distance v border, width, height
    context.fillRect(0, 0, canvas.width, canvas.height)

    // Snake displacement
    positionX += velX;
    positionY += velY;

    // Mirror
    if(positionX < 0){
        positionX = grid;
    }
    if(positionX >grid){
        positionX = 0;
    }
    if(positionY < 0){
        positionY = grid;
    }
    if(positionY > grid){
        positionY = 0;
    }

    // Snake config
    context.fillStyle = "#ff702d"
    for(let i=0; i < snake.length; i++){
        context.fillRect(snake[i].x*grid, snake[i].y*grid, grid-1, grid-1);
        // If the snake touches its body, it returns to its original size
        if (snake[i].x == positionX && snake[i].y == positionY){
            size = 2;
        }
    }

    // Snake moving
    snake.push({x: positionX, y: positionY})
    //console.log(snake[0])

    // Old snake body erasing
    while(snake.length > size){
        snake.shift();
    }

    // Food config
    context.fillStyle = "#b00b0b";
    context.fillRect(foodX*grid, foodY*grid, grid-1, grid-1);

    // Food eating
    if (positionX == foodX && positionY == foodY){
        size ++;
        foodX = Math.floor(Math.random()*grid);
        foodY = Math.floor(Math.random()*grid);
    }
}