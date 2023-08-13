/*

// FUNCTIONS

// f(x) = 2 * x;
// f(2) = 2 * 2 = 4;
// f(10) = 2 * 10 = 20;

function functionName(parameter1, parameter2){
    functionBody
    return returnValue;
};

function hoursToMinutes(hours){
    let value = hours * 60;
    return value;
};

let result = hoursToMinutes(10);
alert(result);



function state(speed){
    if(speed == 0){
        alert("stopped");
    }
    else if(speed > 0 && speed < 100){
        alert("walking");
    }
    else if(speed >= 100){
        alert("running");
    }
};

state(150);



function getBonus(time, livesAmount){
    if(time > 10 && livesAmount < 2){
        alert("Get bonus!");
    }
};

getBonus(10, 2);

*/

// Exercise 1
// Implement a function that will control a game's store.
// She receives the money the player has (number), and the item the player wants to buy (string).
// If the player can make the purchase, the amount of that item receives + 1, otherwise, the program should return "insufficient coins to make the purchase".
// There are 3 items available:(The function must be executed in the console and not in the code).
// Sword (100 coins)
// Shield (200 coins)
// Dagger (300 coins)
// Armor (900 coins)

/*

let coins = 1000;
let swordAmount = 0;
let shieldAmount = 0;
let daggerAmount = 0;
let armorAmount = 0;

function store(coins, item){
    if(item == "sword" && coins >= 100){
        coins -= 100;
        swordAmount += 1;
        console.log("Sword Amount: " + swordAmount + ". Money: " + coins);
    }
    else if(item == "shield" && coins >= 200){
        coins -= 200;
        shieldAmount += 1;
        console.log("Shield Amount: " + shieldAmount + ". Money: " + coins);
    }
    else if(item == "dagger" && coins >= 300){
        coins -= 300;
        daggerAmount += 1;
        console.log("Dagger Amount: " + daggerAmount + ". Money: " + coins);
    }
    else if(item == "armor" && coins >= 500){
        coins -= 500;
        armorAmount += 1;
        console.log("Armor Amount: " + armorAmount + ". Money: " + coins);
    }
    else{
        console.log("Insufficient coins to make the purchase.");
    }
};

let coins = 1000;
let swordAmount = 0;
let shieldAmount = 0;
let daggerAmount = 0;
let armorAmount = 0;

function store(coins, item){
    if(item == "sword" && coins >= 100){
        coins -= 100;
        swordAmount += 1;
        console.log("Succesfully purchased sword. Sword Amount: " + swordAmount + ". Money: " + coins);
    }
    else if(item == "sword" && coins < 100){
        console.log("Insufficient coins to purchase the sword.");
    }
    if(item == "shield" && coins >= 200){
        coins -= 200;
        shieldAmount += 1;
        console.log("Succesfully purchased shield. Shield Amount: " + shieldAmount + ". Money: " + coins);
    }
    else if(item == "shield" && coins < 200){
        console.log("Insufficient coins to purchase the shield.");
    }
    if(item == "dagger" && coins >= 300){
        coins -= 300;
        daggerAmount += 1;
        console.log("Succesfully purchased dagger. Dagger Amount: " + daggerAmount + ". Money: " + coins);
    }
    else if(item == "dagger" && coins < 300){
        console.log("Insufficient coins to purchase the dagger.");
    }
    if(item == "armor" && coins >= 500){
        coins -= 500;
        armorAmount += 1;
        console.log("Succesfully purchased armor. Armor Amount: " + armorAmount + ". Money: " + coins);
    }
    else if(item == "armor" && coins < 500){
        console.log("Insufficient coins to purchase the armor.");
    }
};

*/

/*
// OBJECTS

let player1 = {
    life: 3,
    name: "King",
    points: 99,
    alive: true,
    clothesColor: "black",
    clothesSize: "M"
};

console.log(player1);

// OBJECT INSIDE OBJECT

let player2 = {
    life: 3,
    name: "Queen",
    points: 103,
    alive: true,
    clothes: { 
        clothesColor: "white",
        clothesSize: "P",
        cost: 100,
        new: "true",
    }
};

console.log(player2.name);
console.log(player2.clothes.clothesColor);

player1.life = 4;
console.log(player1.life);

player2.clothes.clothesColor = "blue";
console.log(player2.clothes.clothesColor);

player2.armor = true;
console.log(player2);

delete player2.clothes;
console.log(player2);
*/

// Exercise 2
// Your mission is to create an RPG-type game, for that you need to configure the player with the following attributes: name, lives, points, and magic (boolean), sword (boolean) and magic (number).
// This player will have an object called a map inside it, with the attributes: name, cities, visited cities, found objects. Next, create a new property for the player called tem calice (boolean), and delete it.

let player = {
    name: "Punk",
    lives: 2,
    points: 45,
    isMagic: true,
    sword: false,
    magic: 85,
    map: {
        nameMap: "Saturnalia",
        cities: 40,
        visitedCities: 22,
        foundObjects: 3
    }
};
console.log(player);

player.haveCup = true;
console.log(player);

delete player.haveCup;
console.log(player);