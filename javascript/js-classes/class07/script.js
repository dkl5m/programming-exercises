var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

// Loading images
var bg = new Image();
bg.src = "images/bg.png"
var bird = new Image();
bird.src = "images/bird.png"
var downPipe = new Image();
downPipe.src = "images/downPipe.png"
var ground = new Image();
ground = "images/ground.png"
var pipeFromAbove = new Image();
pipeFromAbove = "images/pipeFromAbove.png"

// Loading sounds
var fly = new Sound();
fly.src = "sounds/fly.mp3"
var scor = new Sound();
scor.src = "sounds/score.mp3"

// Variables
var constant;
var sbp = 100;
var birdX = 33;
var birdY = 200;
var gravity = 1.4;
var score = 0;
var pipe = [];

pipe[0] = {
    x : canvas.width,
    y : 0
}

// Key capture
document.addEventListener("keydown",fly);

// Flying
function fly(){
    bY = bY - 26;
    fly.play();
}

function game(){
    // Game bg -> drawImage(image, X, Y)
    ctx.drawImage(bg,0,0);

    // Creating pipes
    for(let i=0; i<pipe.length; i++){
        // Down pipe position
        constant = pipeFromAbove.height + sbp;
        // Pipe from above position
        ctx.drawImage(pipeFromAbove, pipe[i].x, pipe[i].y);
        // Down pipe config
        ctx.drawImage(downPipe, ppipe[i].x, pipe[i].y + constant);
        // Pipe movimentation
        pipe[i].x = pipe[i].x - 1
        // Creating new pipes
        if(pipe[i].x == 125){
            pipe.push({
                x : canvas.width,
                y : Math.floor(Math.random()*pipeFromAbove.height)-pipeFromAbove.height
            })
        }
    }

    // Ground
    ctx.drawImage(ground,0,canvas.height - ground.height);

    // Bird
    ctx.drawImage(bird, birdX, birdY);
    bY += gravity;

    requestAnimationFrame(game);
}

game();