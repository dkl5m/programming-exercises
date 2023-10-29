"""
01​ - Write a program in which two real numbers,
X and Y, are read and made calls to functions
described below, which must be implemented. In
global scope. The result returned by these
functions must be printed.
    a) A function that takes X and Y as input
    and returns the largest of them;
    b) A function that takes X and Y as input
    and returns their arithmetic mean;

02​ - Write a potentiation function, in which the
input data are: base and exponent (integers).

03​ - Create a calculator that can perform the
highlighted functions of the calculator Windows
10 default.
"""


def functionA(X, Y):
    largest = 0
    smallest = 0

    if X > Y:
        X = largest
        Y = smallest
    elif X < Y:
        Y = largest
        X = smallest
    else:
        largest = smallest = X


def functionB(X, Y):
    mean = (X+Y)/2
    return mean


print("----Functions use----")
value01 = input("Type the first value: ")
value02 = input("Type the second value: ")
functionA(value01, value02)
functionB(value01, value02)

print(f"The largest value is: {functionA}. The mean is {functionB}")
