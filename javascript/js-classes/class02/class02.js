/*
//CONDITIONAL OPERATORS

// == -> equality operator;
// != -> difference operator;
// > -> greater than operator;
// < -> less than operator;
// >= -> greater than or equal to operator;
// <= -> less than than or equal to operator;

let a = 100;
let b = 200;
let c = a < b;

//alert(c);

let d = (a == b);
//alert(d);

let e = (a != b)
//alert(e);

let f = (a >= b);
//alert(f);

let g = (a <= b)
alert(g);


// exercise 1
// create variables a(=1), b(=2) and display it on the console the result of:
// a) a >= b;
// b) a <= b;
// c) a != b;
// d) a == b;

let a = 1;
let b = 2;
let c;

c = (a >= b);
console.log(c);
c = (a <= b);
console.log(c);
c = (a != b);
console.log(c);
c = (a == b);
console.log(c);
*/


/*
// IF AND ELSE

let vel;
vel = 220;

if(vel > 0 && vel < 100){
    alert("Walking");
}
else if(vel > 100){
    alert("Running");
}
else if(vel == 0){
    alert("Stopped");
}

// Exercise 2
// Build a system to display a student's grade, containing 3 possible situations:
// 1) grade > 60: approved;
// 2) score < 60 && > 40: you can take the recovery test;
// 3) grade < 40: failed.

console.log("----Grade_System----");
let grade = 90;

if(grade > 60){
    console.log("APPROVED");
}
else if(grade >= 40 && grade <= 60){
    console.log("You can take the recovery test");
}
else if(grade < 40){
    console.log("FAILED");
};
*/

/*
// BOOLEAN LOGIC

// ! NOT

let magic = !false;

if(magic){
    alert("Magic!");
}
else{
    alert("Not magic!");
};


// && AND

let points = 1000;
let hoursGame = 3;

if(points == 1000 && hoursGame > 2){
    alert("Get bonus!");
}
else{
    alert("No bonus!");
};

// 1 * 1 = 1
// 1 * 0 = 0


// || OR

let points = 1000;
let hoursGame = 1;
let lifes = 1;

if(points < 1000 || lifes < 2){
    alert("Get bonus!");
}
else{
    alert("No bonus!");
};

// 0 + 1 = 1
// 1 + 0 = 1
// 1 + 1 = 1
// 0 + 0 = 0

// Exercise 3
// Create a system that will give the player different types of keys. The program should issue an alert with which key the player will win:
// If he has 3 lives and more than 1000 points = blue key;
// If he has less than 3 lives or less than 1000 points = green key;
// If they have 1000 points and it's not magic = orange key.

let lives = 5;
let magic = true;
let points = 1000;

if(lives >= 3 && points > 1000){
    alert("The player received a blue key!");
}
else if(lives < 3 || points < 1000){
    alert("The player received a green key!");
}
else if(points == 1000 && magic == false){
    alert("The player received a orange key!");
}else{
    alert("The player received a white key!");
};
*/

