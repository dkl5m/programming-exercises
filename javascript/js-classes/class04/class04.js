/*
// METHODS

let player = {
    health: 100,
    happiness: 50,
    play: function(){
        this.happiness += 30;
    },
    eat: function(food){
        if(food == 'orange'){
            this.health += 10;
        }
        if(food == 'grape'){
            this.health += 20;
        }
    }
}

// before the execution 1
    console.log(player);

// execution 1
    player.play();
    player.eat('orange');

// after the execution 1
    console.log(player);

// execution 2
    player.play();
    player.eat('grape');

// after the execution 2
    console.log(player);


// Exercise 1

// Create two properties for the above object:
// coins(initial = 20),
// clothes(initial = no).
// Create a buyout() method to buy a standard outfit that costs twenty coins. If you have enough coins, you buy and the clothes property will have the value 'yes'. Otherwise, an error message will appear on the screen.

let player = {
    health: 100,
    happiness: 50,
    coins: 20,
    clothes: 'no',
    play: function(){
        this.happiness += 30;
    },
    eat: function(food){
        if(food == 'orange'){
            this.health += 10;
        }
        if(food == 'grape'){
            this.health += 20;
        }
    },
    buyClothes: function(){
        if(this.coins >= 15){
            this.coins -= 15;
            this.clothes = 'yes';
        }
        else if(this.coins < 15){
            console.log("Error. Insufficient amount of coins to make the purchase.");
        }
    }
}

// before the execution 1
    console.log(player);

// execution 1
    player.play();
    player.eat('orange');
    player.buyClothes();
    
// after the execution 1
    console.log(player);
*/

/*
// WHILE

// Initiating the sum var
let total = 0;
// Initiating the limit var
let j = 1;
// While j is less than or equal to 10, do:
while(j <= 10){
    total += 1;
    console.log('iteration', total);
    j++;
}

let numberLife = 100;
let coliding = true;

while(coliding){
    numberLife -= 1;
    if(numberLife == 0){
        break;
    }
}


// Exercise 2
// Create a loop that sums all numbers from 0 to 100.

let number = 0;
let sum = 0;

while(number <= 100){
    sum = sum + number;
    number += 1;
    console.log(number);
    console.log(sum);
}
*/

/*
// BREAK

let itens = 0;
let colidingItens = true;

while(colidingItens){
    itens += 1;
    //itens ++;
    //itens = itens + 1;
    console.log(itens);
    if(itens >= 10){
        break;
    }
};
*/

/*
// CONTINUE

let punishment = false;
let colided = true;
let coins = 0;

console.log(coins);

while(colided){
    if(punishment == true){
        continue;
    }

    coins += 1;

    if(coins >= 10){
        break;
    }
}

console.log(coins);


// Exercise 3
// A certain old computer can store numbers up to 9999. Your mission is to create an infinite loop that adds numbers 1 by 1, and create a condition that interrupts the cycle if the number reaches 9999.

let number = 0;

while(true){
    number ++;
      
    if(number >= 9999){
        break;
    };
}

console.log(number);
*/


/*
// FOR
// less dangerous than WHILE, and accepts continue and break too.

// declaration
let x = 10;
for(let i = 0; i < x; i++){
    console.log('iteracao', i);
};

// example

let population = 100;

for(let  iterator = 0; iterator < 10; iterator++){
    population = population + population*0.05;
};

console.log(Math.trunc(population));

*/

// Exercise 4
// Create an algorithm that prints the Celsius-Fahrenheit conversion table to the range desired by the user.
// The algorithm must prompt the user for the upper bound and lower bound of the range.
// Conversion formula: C=5*(F-32)/9

function fahrenheitToCelsius(infLimit, supLimit){
    var Celsius = 0;
    
    for (let iterator = infLimit; iterator < supLimit; iterator++){
        var Fahrenheit = iterator;
        Celsius = (5 * ((Fahrenheit - 32)/ 9));
        console.log(Celsius);
    }
}