import prime

from random import (
    random,
    choice
)

from package1 import principal, secondary
from package1.sub import cubic as other


# NAMED ARGs
"""

def print_name(name, surname, age):
    print("name: ", name)
    print("surname: ", surname)
    print("age: ", age)


surname = "Clara"
age = 20
print_name(surname=surname, age=age, name="Maria")
"""

# STANDARD PATTERN

"""
def print_name(name=None, surname=None, age=None):
    if name is not None:
        print("name: ", name)
        print("surname: ", surname)
        print("age: ", age)
        print("-------------------")
    else:
        print("Please, type your data")
        print("-------------------")


print()
print_name()
print_name("Maria", "Clara", 22)


def print_immobile(name_immobile, number_rooms, garage_spots=None):
    print(name_immobile)
    print("Rooms: ", number_rooms)

    if garage_spots is not None:
        print("Garage has spots", garage_spots)


# Examples of arguments numbers <= parameters numbers
print_immobile("House 3 rooms - SP", 3)
print_immobile("Apartment - MG", 2, 1)

# Examples of arguments numbers > parameters numbers
# print_immobile("Comercial store", 2, 5, "p")
"""

# ARGS - receive arguments that can be stored in a tuple

"""
def print_immobile(name_immobile, number_rooms, garage_spots=None, *phones):
    print(name_immobile)
    print("Rooms: ", number_rooms)

    if garage_spots is not None:
        print("Garage has spots", garage_spots)
    print("Phones: ", phones)


print_immobile("Comercial Store:", 2, 5, "61 5555-5555", "85 4444-4444")


def print_names(*names):
    print(names)

#print_names("Ana", "Bia", "Pietro", "Jack")
list1 = ["Ana", "Bia", "Pietro", "Jack"]
print_names(*list1)
"""

# KWAGS - receive arguments that can be stored in a dictionary
"""
def print_names(**names):
    print(f"{names['name']}{names['surname']}")


print_names(name="Ana", surname="Bia")

# diction = {'name': 'ana', 'surname': 'julia'}
# print_names(diction)
"""

# RECURSION

# IMPERATIVE PARADIGM

"""
def decreaseNumber(int_num):
    while int_num > 0:
        print(int_num)
        int_num -= 1


decreaseNumber(6)
"""
"""
1 - check if our number is not zero
2 - If it is not zero -> decrease one unit

5 (n-1)
  4 (5-1)
    3 (4-1)
      2 (3-1)
        1 (2-1)
          0 (1-1)
"""

# RECURSIVE PARADIGM

"""
def decreaseNumber(int_number):
    print(int_number)
    if int_number > 0:
        # N - 1
        decreaseNumber(int_number - 1)


decreaseNumber(5)
"""

"""
def factorialS(number):  # factorial without recursion

    factorial = 1
    if number == 0:
        return 1
    else:
        for x in range(1, number + 1):
            factorial *= x
        return factorial


# print(factorialS(5))


def factorialR(number):  # factorial with recursion
    if number == 0:  # Stopping criterion
        return 1
    else:
        # recursive call parameter
        return number * factorialR(number - 1)


print(factorialR(5))
"""
"""
# Recursion may be inefficient

3! = 3*2*1
   = 3*2!
   = 3*2*1!

2! = 2*1
   = 2*1!

1! = 1
0! = 1
"""

# MODULE

"""
# import prime
# import random

# from random import (
#    random,
#    choice
# )

# import random as rd

# from random import (
#    random as rd,
#    choice as ch
# )


print(prime.prime(1))
print(random())

list1 = ["rock", 'paper', 'scissors']
print(choice(list1))
"""

#  IMPORT

"""
# from random import * #Import all the module

## module - archives with extension .py - py archives
## packages - directories that contain a set of modules
##            folders with multiple files


# from package1 import principal, secondary
# from package1.sub import cubic as other


print(principal.sum(2, 3))
print(secondary.squared(2))
print(other.cubic(4))
"""
