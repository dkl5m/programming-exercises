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
"""

"""
#       0123456
name = "chicago"

print(name[0]);


for x in range(1, 10, 1):
    print(x);

for x in range(10, 0, -1):
    print(x);


name1 = "chicago";
name2 = "queens";

print(name1, end = " ");
print(name2);

name3 = "chicago";

for x in name3:
    print(x, end = "");


    
# python
x1 = 5;
y1 = 2;

x1, y1 = y1, x1;

print(x1);
print(y1);
"""

# LISTS

"""
list = ["chicago", "queens", "brooklyn", "los angeles"];

list1 = [2, 3, 5, 6, 9];

list2 = [2.0, 3.0, 4.0, 5.0];

list3 = [True, False];

# index     0,  1,         2,  3 -> 4 elements;
list4 = [True, "chicago", 2.5, 4, False];

print(list);
print(list1);
print(list2);
print(list3);
print(list4);

print(list2[1]);
print(type(list4));
print(list2[-1]);
"""

"""
# SLICING - numpy

list1 = [2, 3, 5, 6, 9];
print(list1[::]); # return all index
print(list1[1:]); # return from index to the end of the list;
print(list1[:4]); # return from the beginning of list to index -1;
print(list1[1:3]); # return from first index to second index - 1;
print(list1[1:4:2]); # return from 1 to plus 2;

name = "earth";
print(name[2:4]); # slicing works with strings too;
"""

"""
# FUNCTIONS

list1 = [1, 3, 5];
list2 = [2.5, 3.6, 4.0];
# index =   0,      1,      2;
list3 = ["Name", "Name2", "Name"];

print(list1 + list2);
print(len(list1)); # length of the list;

# Functions that only can used with numerical data;

print(sum(list1)); # sum of all elements => x = 1 + 3 + 5;

print(max(list2)); # largest value of the list;

print(min(list1)); # smallest value of the list;
"""

""""""
# LIST FUNCTIONS

name = "Python course";
value = range(10);

print(name);
print(value);

list10 = list(range(10));
print(list10);

list11 = list(name);
print(list11);

element = 8;
if element in list10:
    print("Element inside the list.");