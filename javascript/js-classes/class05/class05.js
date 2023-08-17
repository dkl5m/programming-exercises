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
*/

// Create an array called map, which stores the villages of an rpg game.
// a) Add the following villages to it: Fire, State, PeopleFear, JF;
// b) Add two more to the end of the list: Jungle, Orchid;
// c) Remove the Orchid village;
// d) Change the village name "Fire" to "CaveMen".

let villages = [];
villages.push('Fire', 'State', 'PeopleFear', 'JF');
console.log(villages);

villages.push('Jungle', 'Orchid');
console.log(villages);

villages.pop();
console.log(villages);

villages[0] = 'CaveMen';
console.log(villages);
