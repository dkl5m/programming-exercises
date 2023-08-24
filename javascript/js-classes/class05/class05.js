/*
// ARRAY

let blankArray = [];

let state = ['won', 'walking', 'running', 'stopped'];
let grades = [10, 20, 30, 40];
let boolean = [true, true, false];

console.log("Array:", state);
console.log("Size:", state.length);

console.log("First element:", state[0]);
console.log("Last element:", state[state.length - 1]);

state[state.length-1] = 'walking';
console.log("Last new element:", state[state.length - 1]);

state.push('New element');
console.log(state);

state.pop();
console.log(state);

// Exercise 1
// Create an array called map, which stores the villages of an rpg game.
// a) Add the following villages to it: Fire, State, PeopleFear, JF;
// b) Add two more to the end of the list: Jungle, Orchid;
// c) Remove the Orchid village;
// d) Change the village name "Fire" to "CaveMen".

let map = [];
map.push('Fire', 'State', 'PeopleFear', 'JF');
console.log(map);

map.push('Jungle', 'Orchid');
console.log(map);

map.pop();
console.log(map);

map[0] = 'CaveMen';
console.log(map);
*/

/*
// ARRAY OPERATIONS

let grades = [40, 20, 50, 43, 56, 22, 34, 43, 44];
console.log("Grades before correction: ", grades);

// Using WHILE

// let i = 0;
// while(i < grades.length){
//     grades[i] += 20;
//     i++;
// };

// Using FOR

// for(i = 0; i < grades.length; i++){
//     grades[i] += 20;
// };


// Using FOR EACH
grades.forEach(function(entry, index, scores){
    grades[index] += 20;
});

console.log("Grades after correction: ", grades);
*/

/*
// Exercise 2
// Suppose that in a RPG game, your inventory is an array with 4 positions, and a certain potion is stored in the inventory as the number 1.
// Your mission is to create a program that goes through your inventory array in search of the number 1.
// If it finds the number 1, it should show on the screen: "Potion found!".

let inventory = [2, 3, 1, 5];

for(i = 0; i < inventory.length; i++){
    if(inventory[i] == 1){
        alert("Potion found! Inventory position: ");
        alert(inventory[i - 1]);
    };
};
*/

/*
// MULTIDIMENSIONAL ARRAYS

let state01 = [['stopped', 'jump'],        ['left', 'right']];

console.log(state01);

// accessing jump position
console.log(state01[0][1]);

state01[0][0] = "anything";
console.log(state01);
state01.pop();
console.log(state01);

state01.push('klsm', 'King');
console.log(state01);
*/

// Exercise 3

// Your task is to create the game "Minefield":
// a) create a 4x4 two-dimensional matrix that will store the game board, white space will be represented by 0 and bomb will be 1. Distribute 0 and 1 by the positions of the matrix.
// b) use variables to store some specific matrix positions, of your choice. Example move1 = field[0][0]:
// c) store all moves in an array called game.
// d) Use a loop of your choice to go through all the positions of the game array, if at least one of the positions has a bomb, the message "you lost" should be displayed, if the whole vector is gone through and no bomb is found, the message "you won" should be displayed as an alert.

// a)
mineField = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1]];
console.log(mineField);

let play1 = mineField[0][1];
let play2 = mineField[1][0];
let play3 = mineField[1][1];
let play4 = mineField[0][0];

plays = [];
plays.push(play1);
plays.push(play2);
//plays.push(play3);
plays.push(play4);
console.log(plays);

for(let i = 0; i < plays.length; i++){
    if(plays[i] == 1){
        alert("You Lost!");
    }
    else if(i == plays.length-1){
        alert("You Won!");
    };
};