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