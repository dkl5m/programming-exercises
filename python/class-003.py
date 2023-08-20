"""
FACTORIAL

4! = 4*3*2*1;
9! = 9*8*7*6*5*4*3*2*1;
0! = 1;
1! = 1;

3! = 3*2*1 = 1*2*3;
"""

"""
# Example 1

factorial = 1;
number = int(input("Type the number to know the factorial: "));

if number < 0:
    print("Doesn't exist negative numbers factorial!");
elif number == 0:
    print(f"{number}! = {factorial}");
else:
    for x in range(1, number + 1):
        factorial *= x;
    print(f"{number}! = {factorial}");
"""

"""
PRIME NUMBER

7/1 = 7; Remainder = 0;
7/7 = 1; Remainder = 0;
"""

"""
print(40 * "-");

number = int(input("Type a number to know if it's a prime number: "));

if number > 1:
    for x in range(2, number):
        if(number % x) == 0:
            print(f"{number} is not a prime number");
            break;
    else:
        print(f"{number} is a prime number");
else:
    print(f"{number} is not a prime number. Number less than or egual to 1");

print(40 * "-");
"""

"""
# CONTINUE

for x in range(10):
    if x == 3:
        continue; # jump to the next repeating loop.
    print(x);
"""

"""
# PASS

if x == 5:
    pass; # ignore the identation error. Careful using it.

print("Hello world");
"""


# ASSIGNMENT

"""
sites to train logics and compete online:

urionlinejudge.com.br - URI
hackerrank.com - hacker rank
codechef.com - code chef
codeingame.com - code game
"""

x = 0;
print(f"1st x value: {x}");
x = 1;
print(f"2nd x value: {x}");
x = x + 1;
print(f"3rd x value: {x}");
x -= 1;
print(f"4rd x value: {x}");
x *= 3;
print(f"5nd x value: {x}");
x **= 3;
print(f"6nd x value: {x}");
x = x % 3;
print(f"7nd x value: {x}");
x = x / 3;
print(f"8nd x value: {x}");
x = x // 5;
