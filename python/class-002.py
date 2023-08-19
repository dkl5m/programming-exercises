"""
LOOPS

WHILE, FOR, DO WHILE*
 
obs : python doesn't have switch case or do while.

# WHILE

a = 0;

while a <= 5:
    print(a);
    a = a + 1; 

print("Final result of a: ", a);
"""

"""
# WHILE WITH BREAK


a = 0;

while a <= 5:
    print(a <= 5);
    print(a);
    if a == 3:
        break;
    a = a + 1;

print("Value: ", a);
print(a <= 5);
"""

"""
# WHILE AND ELSE

a = 0;

while a <= 5:
    print(a <= 5);
    print(a);
    a = a + 1;
else:
    print(f"'a' is not greater than or equal to 5. 'a' value: {a}");
"""

"""
# FOR

for x in range(6): # range(6) means that it start from 0 until we have 6 digits.
    print(x);

for x in range(2, 5):
    print(x);

for x in range(0, 6, 1): # range(6);
    print(x);

for x in range(6): # for(x = 0 x <= 5; x++);
    print(x);
else:
    print("End!");
"""

# Exercise
# PASSWORD GENERATOR

# uppercase and lowercase
# numbers, symbols and spaces

"""
security = key
5ecur1ty = senha

hex
1 = 1;
2 = 2;
...
9 = 9;
10 = A;
11 = B;
12 = C;
13 = D;
14 = E;
15 = F;
"""
"""
# NOT GOOD PATTERN

key = input("Write the base to your password: ");

password = "";
for letter in key:
    if letter in "Aa": password = password + "10";
    elif letter in "Bb": password = password + "11";
    elif letter in "Cc": password = password + "12";
    elif letter in "Dd": password = password + "13";
    elif letter in "Ee": password = password + "14";
    elif letter in "Ff": password = password + "15";
    elif letter in "Rr": password = password + "#";
    elif letter in "Ss": password = password + "%";
    elif letter in "Mm": password = password + "$";
    else: password = password + letter;

print(password);
"""

"""
# Better

key = input("Type the base to your password: ");

password = "";
for letter in key:
    if letter in "Aa": password = password + "1";
    elif letter in "Bb": password = password + "@";
    elif letter in "Cc": password = password + "2";
    elif letter in "Dd": password = password + "3";
    elif letter in "Ee": password = password + "4";
    elif letter in "Ff": password = password + "5";
    elif letter in "Rr": password = password + "#";
    elif letter in "Ss": password = password + "%";
    elif letter in "Mm": password = password + "$";
    else: password = password + letter;

print(password);
"""

"""
Exercise - Changing vars

# Changing vars in python

x = input("Insert the x value: ");
y = input("Insert the y value: ");

# Creating a temp var

temp = x;
x = y;
y = temp;

print(f"The x value is {x} and the y value is {y}, after the change.");
"""

"""
# Exercise - verify numeric signal

number = int(input("Type a number:"));

if int(number) > 0:
    print(f"{number}: positive number.");
elif int(number) == 0:
    print(f"{number}: neutral number.");
else:
    print(f"{number}: negative number.");
"""

"""
DO WHILE
"""
"""
# Guess the number

guess = 0;
number = 9;


#   {
while True:
    print("What is the correct number?");
    guess = int(input());
#   }DO WITHOUT VERIFYING
#   {
    if guess == number:
        print("Congratulations, you won.");
        break;
    else:
        print("You lost");
#   }VERIFY
#   {
else:
    print("Error in app.");
    print(bol(guess));
#   }USEFUL WHILE DEVELOPING
"""

"""
# PAIR NUMBER

# How to know it

first = 5;
second = 2;

print(first%second);

# 0, 2, 4, 6, 8, ... PAIR
# 0/2, 2/2, 4/2, ... (1, 0)
"""

print(20*"-");
number = int(input("Type a number to know if it's pair! "));

if(number % 2) == 0:
    print(f"{number} is pair");
else:
    print(f"{number} is impair");

print(20*"-");