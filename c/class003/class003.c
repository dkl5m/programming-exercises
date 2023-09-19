#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// CONST

// Exercise 1
// Print different types of variables

/*
#define CONST 5
#define FLOAT 9.3
#define LETTER 'a'

int main(){
    const int NUM = 10;

    printf("%d \n", CONST);
    printf("%f \n", FLOAT);
    printf("%c \n", LETTER);
    printf("%d \n", NUM);
    
    return 0;
}
*/

// VECTOR

// Exercise 1
/*
#define SIZE 2 // defining const

int main(){
    
    // defining vectors
    int int_vector[] = {1,2,3,4};
    float float_vector[3] = {1.5, 2.0, 2.5};
    char char_vector[SIZE] = {'a', 'b'};

    // modifying value per assignment
    int_vector[0] = 9;

    // modifying value with var
    float new_value = 5.8;
    float_vector[2] = new_value;

    // modifying value with user
    printf("Type a new letter: ");
    scanf(" %c", &char_vector[0] );

    // printing vectors
    int i = 0;
    printf("\nvector 1: \n");
    for(i = 0; i < 4; i++){
        printf("%d\n", int_vector[i]);
    }

    printf("\nvector 2: \n");
    for(i = 0; i < 3; i++){
        printf("%f\n", float_vector[i]);
    }
    
    printf("\nvector 3: \n");
    for(i = 0; i < SIZE; i++){
        printf("%c\n", char_vector[i]);
    }

    // reading values for all the vector
    printf("\n Type integers: \n");
    for(i = 0; i < 4; i++){
        printf("Reading in vector[%d]:", i);
        scanf("%d", &int_vector[i]);
    }

    // printing this updated vector
    for(i = 0; i < 4; i++){
        printf("%d\n", int_vector[i]);
    }

    return 0;
}
*/

// STRING

// Exercise 1
// Program to show different types of string

/*
int main(){

    // defining different forms strings
    char word1[] = "cow";
    char word2[5] = "ball";
    char word3[] = {'a', 'b', 'c', 'd', '\0'};
    char word4[6] = {'p', 'h', 'o', 'n', 'e', '\0'};

    // printing string (without spaces)
    printf("%s \n", word1);

    // reading a string (without spaces)
    printf("Type a word with 4 letters: \n");
    fflush(stdin);
    scanf(" %s", word2);
    
    // reading a string (with spaces)
    char fruit[255];
    fflush(stdin);
    printf("Type the name of a fruit: \n");
    fgets(fruit, sizeof(fruit), stdin);

    //printing the read fruit
    printf("Read fruit:");
    puts(fruit);
    
    return 0;
}
*/

// MATRIX

// Exercise 1
// Make a program that ask to build a matrix 2x3

/*
#define ROW 2
#define COLUMN 3

int main(){
    
    // Create matrix
    int matrix[ROW][COLUMN];
    int i, j;

    // Read the values to matrix
    for(i = 0; i < ROW; i++){
        for(j = 0; j < COLUMN; j++){
            scanf("%d", &matrix[i][j]);
        }
        printf("\n");
    }

    // Print the values to matrix
    for(i = 0; i < ROW; i++){
        for(j = 0; j < COLUMN; j++){
            printf("%d", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
*/

// VOID FUNCTION

// Exercise 1
// Make an example with a void function

/*
// void function (Don't return anything on the end)
void drawSeparator(){
    printf("\n--------------\n");
}

int main(){
    // Call the function and execute what is inside it
    drawSeparator();
    printf("Hi");
    drawSeparator();
    printf("How you doin?");
    drawSeparator();
    printf("It's the end! Go away! It's over!");
    drawSeparator();
    
    return 0;
}
*/

// LOCAL AND GLOBAL SCOPE

// Exercise 1
// Void function without parameter in local scope

/*
// Void function
void printA(){
    int a = 10;
    printf("'A' value in the function: %d\n", a);
}

int main(){
    // Define 'a' value in main scope
    int a = 15;
    printf("'A' value outside of the function: %d\n", a);

    printA();
    
    // Print printA function 'a' var
    printf("'A' value outside of the function: %d\n", a);

    return 0;
}
*/

/*
// Exercise 2
// Void function in global scope

int globalExample = 20;

// Void function
void printA(){
    int a = 10;
    printf("'A' value in the function: %d\n", a);
    globalExample = 50;
}

int main(){
    // Define 'a' value in main scope
    int a = 15;
    printf("'A' value outside of the function: %d\n", a);
    printf("Global example value: %d\n", globalExample);

    printA();
    
    // Print printA function 'a' var
    printf("'A' value outside of the function: %d\n", a);
    printf("Global example NEW value: %d\n", globalExample);

    return 0;
}
*/

// RECURSION

/*
// Exercise 1
// Recursion example

int value = 0;

void addOneUntil10(){
    // If value is less than 10
    if(value < 10){
        // Print on screen
        printf("%d\n", value);

        value++;

        // Call function again
        addOneUntil10();
    }
}

int main(){
        // Call the function once
        addOneUntil10();

        // Finish the recursion
        printf("End");

        return 0;
    }
*/

// FUNCTIONS WITH RETURN

int return10(){
    int a = 10;
    return a;
}

int returnFloat(){
    float a = 5.5;
    return a;
}

char returnLetter(){
    return 'a';
}

int main(){
    printf("Return 10 of function: %d\n", return10());
    
    float float_number = returnFloat();
    printf("Return float: %f\n", float_number);
    
    printf("Return letter: %c\n", returnLetter());    
    return 0;
}