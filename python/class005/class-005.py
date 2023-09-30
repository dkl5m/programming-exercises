# POO

# Imperative Paradigm

"""
Imperative Paradigm - Fortran - Sequence, Decision, Iteration - 1st created
Structured Paradigm - C - Better syntax - Structs
Procedural Paradigm - Python

reuse and cohesion
"""
"""
def Register(name, age, ppr, email):
    patient = {'name': name, 'age': age, 'ppr': ppr, 'email': email}
    return patient
"""

# Object-Oriented Paradigm

"""
Structure concepts

Class - A set of objects with the same characteristics,
        CamelCase
Object - Representation of the real world as a type of the data
         of the class
Constructor - Function created implicitly with the same name as the class,
              Python do it in it's internals
Attribute - Variables of a class
"""


class Patient:
        # __init__ access the constructor
    def __init__(self, name, age, ppr, email):
            # self = call the actual class
        print("Constructor accessed")
            # call the class attributes
        self.name = name
        self.age = age
        self.ppr = ppr
        self.email = email

"""
simulation (CS) - idea of represent the real world in the computational
world

Discret-event simulation (change in time) -> OOP

Relationship -> highlighting functions(methods) and variables(attributes)

-----------------------------------------------------------
Class:

Class is a structure that abstracts a set of objects with similar
characteristics. Defining the behavior of your objects through structures:
1 - Attributes
2 - Methods

The class defines an abstract data type
"""

# abstraction
# reuse and cohesion
# coupling, heritage, polymorphism, semantic gap
"""
Fundamental concepts

Abstraction
Process by which attributes of an object are isolated, considering what certain groups of objects have in common.

Reuse
There is no worse practice in programming than repeating code
"""
