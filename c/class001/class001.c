#include <stdio.h>
#include <stdlib.h>

/*

// Exercise 001

int main(){
    int a = 10; // defining a
    int b = 20; // defining b
    int result = a + b; // defining result

    printf("Result: %d", result); // show the result value
    return 0;
}
*/

/*
// Exercise 002

int main(){
    int a = 10; // defining a
    int b = 20; // defining b
    int c = 30; // defining c
    int result = a + b + c; // defining result

    printf("Result: %d", result); // show the result value
    return 0;
}
*/

/*
// Exercise 003

int main(){
    int a = 10; // defining a
    int b = 20; // defining b
    int result = b / a; // defining result

    printf("Result: %d", result); // show the result value
    return 0;
}
*/

/*
// Exercise 004

int main(){
    float a = 1.5; // defining a
    float b = 2.5; // defining b
    float result = b * a; // defining result

    printf("Result: %.2f", result); // show the result value
    return 0;
}
*/

/*
// Exercise 005

int main(){
    float a = 1.5; // defining a
    float b = 2.5; // defining b
    float result = b / a; // defining result

    printf("Result: %.2f", result); // show the result value
    return 0;
}
*/

/*
// Exercise 006

int main(){
    int a; // defining a
    int b; // defining b

    printf("Type the 'a' value: ");
    scanf("%d", &a);
    printf("Type the 'b' value: ");
    scanf("%d", &b);

    int result = b + a; // defining result

    printf("Result: %d", result); // show the result value
    printf("\n");
    return 0;
}
*/

/*
// Exercise 007

int main(){
    int a; // defining a
    int b; // defining b

    printf("Type the 'a' value: ");
    scanf("%d", &a);
    printf("Type the 'b' value: ");
    scanf("%d", &b);

    int result = b / a; // defining sum

    printf("Result: %d", result); // show the result value
    printf("\n");
    return 0;
}
*/

/*
// Exercise 008

int main(){
    float a; // defining a
    float b; // defining b

    printf("Type the 'a' value: ");
    scanf("%f", &a);
    printf("Type the 'b' value: ");
    scanf("%f", &b);

    float result = b * a; // defining sum

    printf("Result: %.2f", result); // show the result value
    printf("\n");
    return 0;
}
*/

/*
// Exercise 009

int main(){
    char a; // defining a
    char b; // defining b

    printf("Type the 'a' value: ");
    scanf(" %c", &a);

//   usually, people tell to clear the buffer with (win: fflush(stdin), linux: __fpurge(stdin)),
//   but we don't really need to use it.

//   numeric field input (%d, %f etc) ignores leading spaces and end-line characters (\r and \n);

//   string input (%s) ignores leading spaces and end-of-line characters (\r and \n);

//   character input (%c) does NOT ignore leading spaces and end-of-line characters (\r and \n),
//   but this is easily circumvented using a " %c" format, ie with a space before the %c;
//   this previous space "eats" all spaces, tabs and end of line, before reading the next character,
//   eliminating the need to use fflush and fpurge.


    printf("Type the 'b' value: ");
    scanf(" %c", &b);
    //__fpurge(stdin);

    printf(" %c %c", a, b); // show the result value
    printf("\n");
    return 0;
}
*/

// CONDITIONALS

/*
// Exercise 001
// Make a program that receives the user age and displays
// if he is minor, have to enlist or if he is of legal age

int main(){
    int age; // defining age

    printf("Type your age: ");
    scanf("%d", &age); // read age

    if(age < 17){
        printf("Minor!\n");
    }else if(age == 18){
        printf("You have to enlist!\n");
    }else{
        printf("Of legal age!\n");
    }

    return 0;
}
*/

/*
// Exercise 002
// Make a program that receives two integers and shows if their sum
// is bigger than or equal to 10 or if it is smaller
int main(){
    int number1; // defining number1
    int number2; // defining number2
    printf("Type the 1st number: ");
    scanf("%d", &number1);
    printf("Type the 2nd number: ");
    scanf("%d", &number2);

    int sum = number1 + number2;
    
    if(sum >= 10){
        printf("Sum value is bigger than or equal to 10!\n");
    }else{
        printf("Sum value is smaller than 10!\n");
    }

    return 0;
}
*/

/*
// Exercise 003
// Make a program that receives two integers and print on
// the screen which one is bigger or if they are equal

int main(){
    int number1;
    int number2;

    printf("Type the 1st integer: ");
    scanf("%d", &number1);
    printf("Type the 2nd integer: ");
    scanf("%d", &number2);
    
    if(number1 > number2){
        printf("%d, the 1st integer, is bigger than %d, the 2nd integer!\n", number1, number2);
    }
    else if(number2 > number1){
        printf("%d, the 2nd integer, is bigger than %d, the 1st integer!\n", number2, number1);
    }
    else{
        printf("the two integers are equal!\n");
    }

    return 0;
}
*/

/*
// Exercise 004
// Make a program that reads an integer and informs if
// it is even or not

int main(){
    int number;

    printf("Type an integer: ");
    scanf("%d", &number);

    if(number % 2 == 0){
        printf("The number is even!\n");
    }else{
        printf("The number is odd!\n");
    }

    return 0;
}
*/

// LOGIC CONNECTIVES

/*
// Exercise 005
// Make a program that reads the age of two people and print on the screen
// if they can enter on a rave (must be of legal age)

int main(){
    int number1;
    int number2;

    printf("Type 1st person age: ");
    scanf("%d", &number1);
    printf("Type 2nd person age: ");
    scanf("%d", &number2);

    if(number1 > 17 && number2 > 17){
        printf("Ok!\n");
    }else{
        printf("Problem!\n");
    }

    return 0;
}
*/

/*
// Exercise 006
// Make a program that reads the age of two people and print on the screen
// if they can enter on a cinema (one must be of legal age)

int main(){
    int number1;
    int number2;

    printf("Type 1st person age: ");
    scanf("%d", &number1);
    printf("Type 2nd person age: ");
    scanf("%d", &number2);

    if(number1 > 17 || number2 > 17){
        printf("Ok!\n");
    }else{
        printf("Problem!\n");
    }

    return 0;
}
*/

/*
// Exercise 007
// Make a program that reads an integer and print on the screen
// if it is between 0 and 10

int main(){
    int number;

    printf("Type an integer: ");
    scanf("%d", &number);

    if(number > 0 && number < 10){
        printf("The number is between 0 and 10!\n");
    }else{
        printf("The number is not between 0 and 10!\n");
    }

    return 0;
}
*/

/*
// Exercise 008
// Make a program that reads three integers and print on the screen
// if they are all bigger than 10

int main(){
    int number1;
    int number2;
    int number3;

    printf("Type the 1st integer: ");
    scanf("%d", &number1);
    printf("Type the 2nd integer: ");
    scanf("%d", &number2);
    printf("Type the 3rd integer: ");
    scanf("%d", &number3);

    if(number1 > 10 && number2 > 10 && number3 > 10){
        printf("The three integers are bigger than 10!\n");
    }else{
        printf("The three integers are not bigger than 10!\n");
    }

    return 0;
}
*/

/*
// Exercise 009
// Make a program that reads two integers and print on the screen
// if some of them are bigger than 10

int main(){
    int number1;
    int number2;

    printf("Type the 1st integer: ");
    scanf("%d", &number1);
    printf("Type the 2nd integer: ");
    scanf("%d", &number2);

    if(number1 > 10 || number2 > 10){
        printf("One of the integers is bigger than 10!\n");
    }else{
        printf("None of the integers is bigger than 10!\n");
    }

    return 0;
}
*/

/*
// Exercise 010
// Make a program that reads two integers and print on the screen
// if the sum of them is between 0 and 10 or if it is even

int main(){
    int number1;
    int number2;
    int sum;

    printf("Type the 1st integer: ");
    scanf("%d", &number1);
    printf("Type the 2nd integer: ");
    scanf("%d", &number2);
    sum = number1 + number2;

    if((sum > 0 && sum < 10) || (sum % 2 == 0)){
        printf("The sum is between 0 and 10 or is even!\n");
    }else{
        printf("The sum is not between 0 and 10 or is not even!\n");
    }

    return 0;
}
*/
