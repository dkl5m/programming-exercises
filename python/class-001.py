"""
# Numbers
# integers - int: ..., -2, -1, 0, 1, 2, ...
# float: -3, 3.4
# complex: 1+2j

# Variables
# keep data values
# x = 5; x keep the value 5

# w = 'Ana' = "Ana"
# A-z, 0-9, _
# height, Height, HEIGHT


h, j, l = 1, 3, 5
print(h)
print(j, l)

a = b = c = 4
print(a, b, c)

h = b + h
print(h)

x = 'Ana'
#l = x + b
"""

# Strings
# a = """Hello, this is
# a Python course"""
# """
# print(a)
"""
b = ' Hello '
print(b.strip())
print(b.lower())
print(b.upper())

c = 'World'
d = b + c
print(d)
"""

"""
Type
a = 'Hello'
b = 1
c = 2.
d = 1 + 2j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""

"""
# Casting
# int
x = int(2)
y = int(2.5)
z = int('2')
print(x, y, z)

# float
x = float(2)
y = float(2.5)
z = float('2')
print(x, y, z)

# str
t = str('s1')
r = str(2)
z = str(2.3)

print('Var t type is: ', type(t))
print('Var r type is: ', type(r))
print('Var z type is: ', type(z))
"""

"""
# Scope
# Var scope
x = 5; # global var

def function():
    x = 3 # local var
    print('Local var value:', x)

function()
print('Global var value:', x)

# Best way to name a variable
name = 'Mann'
height = 1.74
cpf = "000.000.000-00"
age = 24

# Arithmetic operators
# sum +
# subtraction -
# multiplication *
# division /
# module %
# exp **
# int div //

x = 2
y = 4
a = x + y
b = x - y
c = x * y
d = x / y
e = x % y
f = x ** y
g = x // y
print(a, b, c, d, e, f, g)
"""

# Boolean: true or false
# Logical operators
# and, or, not

# True table
# And
# false and false = false
# false and true = false
# true and false = false
# true and true = true

# Or
# false or false = false
# false or true = true
# true or false = true
# true or true = true

# Not
# Not true = false
# Not false = true

"""
# Input function - save user data

# 1st way
print("What is your name? ")
name = input()
print("Hello, ", name)

# 2nd way
# age = input("How old are you? ")
# print("You're", age, "old!")

name = input("What is your name? ")
age = input("How old are you? ")
print("Your name is {0} and you're {} years old!".format(name, age))

# 3rd way
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Your name is {name} and you're {age} years old!")
"""

"""
# Comparison operators

# Equality operator ==
# Dif operator !=
# greater than operator >
# less than operator <
# greater than or equal to >=
# less than operator or equal to <=

x = 3 #int
y = 5
z = 3.0 #float
w = 8

print(x == z)
print(x != z)
print(w > x)
print(w < x)
print(x >= z)
print(x <= z)
print(x >= y)

# Associative operators
name = "Kang"

# In Operator - x in y
# Not in Operator - x not in y

x = "pernambuco"
y = "nam"
print(y in x)
print("nam" in x)
print('per' in x)
print('camper' in x)
print('per' not in x)

# If, else or elif (else if)

x = 5
y = 5

if(x < y):
    print("y is greater than x")
elif(x > y):
    print("x is greater than y")
else:
    print("x is equal to y")
"""

"""
x = 5
y = 4
z = 3

# Smaller version
# if(x < y): print("y is greater than x")

# print("B") if x > y else print("A"); #Ternary operator

if x > y:
    if x > z:
        print("x greater than y and z")
"""

"""
LOOPS

# WHILE, FOR, DO WHILE
# obs : python doesn't have switch case or do while.

# WHILE

a = 0

while a <= 5:
    print(a)
    a = a + 1

print("Final result of a: ", a)
"""

"""
# WHILE WITH BREAK


a = 0;

while a <= 5:
    print(a <= 5)
    print(a)
    if a == 3:
        break
    a = a + 1

print("Value: ", a)
print(a <= 5)
"""

"""
# WHILE AND ELSE

a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print(f"'a' is not greater than or equal to 5. 'a' value: {a}")
"""

"""
# FOR

for x in range(6): # range(6) means that it start from 0 until we have 6 digits
    print(x)

for x in range(2, 5):
    print(x)

for x in range(0, 6, 1): # range(6)
    print(x)

for x in range(6): # for(x = 0 x <= 5; x++)
    print(x)
else:
    print("End!")
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

key = input("Write the base to your password: ")

password = ""
for letter in key:
    if letter in "Aa": password = password + "10"
    elif letter in "Bb": password = password + "11"
    elif letter in "Cc": password = password + "12"
    elif letter in "Dd": password = password + "13"
    elif letter in "Ee": password = password + "14"
    elif letter in "Ff": password = password + "15"
    elif letter in "Rr": password = password + "#"
    elif letter in "Ss": password = password + "%"
    elif letter in "Mm": password = password + "$"
    else: password = password + letter

print(password)
"""

"""
# Better

key = input("Type the base to your password: ")

password = ""
for letter in key:
    if letter in "Aa": password = password + "1"
    elif letter in "Bb": password = password + "@"
    elif letter in "Cc": password = password + "2"
    elif letter in "Dd": password = password + "3"
    elif letter in "Ee": password = password + "4"
    elif letter in "Ff": password = password + "5"
    elif letter in "Rr": password = password + "#"
    elif letter in "Ss": password = password + "%"
    elif letter in "Mm": password = password + "$"
    else: password = password + letter

print(password)
"""

"""
Exercise - Changing vars

# Changing vars in python

x = input("Insert the x value: ")
y = input("Insert the y value: ")

# Creating a temp var

temp = x
x = y
y = temp

print(f"The x value is {x} and the y value is {y}, after the change.")
"""

"""
# Exercise - verify numeric signal

number = int(input("Type a number:"))

if int(number) > 0:
    print(f"{number}: positive number.")
elif int(number) == 0:
    print(f"{number}: neutral number.")
else:
    print(f"{number}: negative number.")
"""
