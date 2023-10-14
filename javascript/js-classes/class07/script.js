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