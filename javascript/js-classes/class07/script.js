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
var eec = 100;
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

    // Ground
    ctx.drawImage(ground,0,canvas.height - ground.height);

    // Bird
    ctx.drawImage(bird, birdX, birdY);
    bY += gravity;

    requestAnimationFrame(game);
}

game();