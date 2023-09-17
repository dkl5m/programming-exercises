#include <stdio.h>
#include <stdlib.h>

/*
// SWITCH CASE

// Exercise 1
// Make a program that shows the options of coffee, reads the chosen option
// and show it on the screen

int main(){

    //Menu
    printf("    Menu         \n");
    printf("1 - Espresso      \n");
    printf("2 - Cappuccino   \n");
    printf("3 - Macchiato    \n");
    printf("Choose an option:\n");

    //Read the chosen option. Can be used char, just switching the var type to c
    int option;
    scanf("%d", &option);

    //Select the case. If used char, case must be -> case 'a':
    switch(option){
        case 1:
            printf("Chosen Espresso.\n");
            break;
        case 2:
            printf("Chosen Cappuccino.\n");
            break;
        case 3:
            printf("Chosen Macchiato.\n");
            break;
        default:
            printf("Option not available.\n");
            break;
    }

    return 0;
}
*/

// Exercise 2

// Make a calculator program that reads two values ​​and shows the options
// to add or subtract. After selecting the option, the result will be
// shown on the screen, based on a switch

/*
int main(){
    int number1, number2, option;

    printf("Type 1st number: ");
    scanf("%d", &number1);
    printf("Type 2st number: ");
    scanf("%d", &number2);

    printf("Choose an option: \n");
    printf("1 - Add: \n");
    printf("2 - Subtract: \n");
    scanf("%d", &option);

    switch(option){
        case 1:
            printf("Chosen 'Add': \n");
            printf("Result: %d!\n", number1 + number2);
            break;
        case 2:
            printf("Chosen 'Subtract': \n");
            printf("Result: %d!\n", number1 - number2);
            break;
        default:
            printf("Option not available!");
            break;
    }


    return 0;
}
*/

/*
// RANDOM NUMBER FROM 0 TO 9

// Exercise 001
// Make a program that returns a random number

int main(){
    // Use the actual time like a seed
    srand(time(NULL));

    // Create a random number from 0 to 9
    int r = rand() % 10;

    // Print the generated number
    printf("Generated number: %d\n", r);

    return 0;
}
*/

/*
// RANDOM NUMBER WITH INTERVAL

// Exercise 001
// Make a program that returns a random number between
// 9 and 14

int main(){
    // Use the actual time like a seed
    srand(time(NULL));

    int min = 5;
    int max = 14;

    // Create a random number from 5 to 14
    int r = (rand() % (max - min + 1)) + min;

    // Print the generated number
    printf("Generated number: %d\n", r);

    return 0;
}
*/

// Exercise 3
// Write a program that rolls 3 random dice (six sides)
// and displays the result of the sum of the 3 values
// generated on the screen

/*
int main(){
    srand(time(NULL));

    int min = 1;
    int max = 6;
    int sum = 0;

    int r1 = (rand() % (max - min + 1)) + min;
    int r2 = (rand() % (max - min + 1)) + min;
    int r3 = (rand() % (max - min + 1)) + min;

    sum = r1 + r2 + r3;
    printf("Values: %d, %d, %d\n", r1, r2, r3);
    printf("Sum: %d\n", sum);

    return 0;
}
*/

// WHILE
// Used for validation

// Exercise 1
// Write a program that print the values from 0 to 10
// using while

/*
int main(){
    int i = 0;

    while(i <= 10){
        printf("%d \n", i);
        i++; // can increase the i, with i += value
    }

    return 0;
}
*/

// Exercise 2
// // Write a program that print the values from 10 to 0
// using while

/*
int main(){
    int i = 10;

    while(i > -1){
        printf("%d \n", i);
        i-=1; // can increase the i, with i += value
    }

    return 0;
}
*/

// Exercise 3
// Write a program that stop if a number is equal to 10
// using while and validation

/*
int main(){
    int i = 0;

    while(i != 10){
        printf("Type 10:");
        scanf("%d", &i);
    }

    printf("End!\n");

    return 0;
}
*/

// Exercise 4
// Write a program that stop if a number is bigger than 10
// using while and validation

/*
int main(){
    int i = 0;

    while(i < 10){
        printf("Type a number bigger than 10: ");
        scanf("%d", &i);
    }

    printf("End!");

    return 0;
}
*/

// Exercise 5
// Write a program that stop when if one of the numbers is
// bigger than 10

/*
int main(){
    int a = 0, b = 0;

    while(a < 10 || b < 10){
        printf("Type two numbers bigger than 10\n");

        printf("Type 1st number bigger than 10: ");
        scanf("%d", &a);
        
        printf("Type 2nd number bigger than 10: ");
        scanf("%d", &b);
    }

    printf("End!\n");

    return 0;
}
*/

// DO WHILE

// Exercise 1
// Write a program to explain the functionality of Do While

/*
int main(){
    int i = 10;

    do{
        printf("It will be executed at least one time.\n");
        printf("Even if the condition is false.\n");
    }while(i < 5);
    
    return 0;
}
*/

// Exercise 2

// Write a program that print the values from 50 to 0
// decreasing from 6 to 6, using while

/*
#include <stdio.h>

int main()
{
    int i = 50;
    
    while(i > -1){
        printf("%d\n", i);
        i-=6;
    };
    
    return 0;
}
*/

// Exercise 3

// Write a program that prints even numbers
// from 10 to a number entered by the user

/*
#include <stdio.h>

int main()
{
    int i = 10;
    int a = 0;
    
    printf("Type an integer: ");
    scanf("%d", &a);
    
    while(i <= a){
        if(i % 2 == 0){
        printf("%d\n", i);
    }
        i+=1;
    };
    
    return 0;
}
*/

// Exercise 4

// Write a program that prints the sum of two
// integers between 5 and 10, just when the
// two entered numbers are in the range

/*
int main()
{
    int a = 0;
    int b = 0;
    int sum = 0;

    while(!(a > 5 && a < 10) || !(b > 5 && b < 10)){
        printf("Integers between 5 and 10: ");
        
        printf("Enter the 1st integer: ");
        scanf("%d", &a);

        printf("Enter the 2nd integer: ");
        scanf("%d", &b);
    };
    
    sum = a + b;
    printf("Sum: %d\n", sum);

    return 0;
}
*/

// FOR

// Exercise 1
// Make a program using FOR to print from 0 to 10

/*
int main(){
    int i = 0;
    for(i = 0; i < 11; i++){
        printf("%d\n", i);
    };

    return 0;
}
*/

// Exercise 2
// Make a program that prints the sum of all numbers from 0
// to 10, adding the actual value of I in the sum var, each
// repeat of FOR loop

/*
int main(){
    int i, sum = 0;

    for(i = 0; i < 11; i++){
        printf("i = %d (sum: %d)\n", i, sum);
        sum += i;
    }

    printf("sum: %d\n", sum);

    return 0;
}
*/

// Exercise 3
// Make a program that print the multiplication table from a number
// entered by the user

/*
int main(){
    int i, multiplication_table = 0;
    printf("Type a integer: ");
    scanf("%d", &multiplication_table);
    printf("----- %d MULTIPLICATION-TABLE -----\n", multiplication_table);

    for(i = 1; i < 11; i++){
        printf("%d * %d = %d\n", i, multiplication_table, i * multiplication_table);
    }

    return 0;
}
*/

// Exercise 3
// Make a program that the user enter the initial value, final value,
// the pass, and print all the values from the range entered by the user

/*
int main(){
    int initial_value, final_value, pass, i = 0;
    printf("Type the 1st integer: ");
    scanf("%d", &initial_value);
    printf("Type the 2nd integer: ");
    scanf("%d", &final_value);
    printf("Type the pass: ");
    scanf("%d", &pass);
    printf("----- RANGE -----\n");
    

    for(i = initial_value; i <= final_value; i += pass){
        printf("%d\n", i);
    }

    return 0;
}
*/
