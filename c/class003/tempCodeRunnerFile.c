#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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

/*
    for(int i = 0; i < 3; i++){
        int r = (rand() % (max - min + 1)) + min;

        int sum = sum + r;
        printf("%d\n", r);
        printf("%d\n", sum);
}*/
    return 0;
}