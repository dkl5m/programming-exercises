"""
class Patient:
    pass
"""

"""
class Square:

    def __init__(self, side):
        self.__side = side
        self.__area = side * side

    def return_area(self):
        print(self.__area)


square = Square(3)
square.return_area()
square.area = 7  # Dynamic variable
square.return_area()
print(square.__dict__)
square._Square__area = 16  # Name mangling
# Don't use it unless you are testing the code

square.return_area()
"""
"""
NAME MANGLING -> _Class__attribute
    used when you're testing your code
"""


# GETTERS AND SETTERS
"""
Used in protected and private attribute cases
Call all the attributes like they were public
"""

"""
class Student:
    def __init__(self, name, age, registration):
        self.__name = name
        self.__age = age
        self.__registration = registration
        self.__grades = None

    # getter - python way
    @property
    def name(self):
        return self.__name

    # setter - python way
    @name.setter
    def name(self, name):
        self.__name = name

    # getter - normal way
    def get_age(self):
        return self.__age

    # setter - normal way
    def set_age(self, age):
        self.__age = age


student1 = Student('Jose', 17, 123456)

print(student1.name)
student1.name = 'Joseph'
print(student1.name)
"""

# SIMPLE HERITAGE


class Person:
    def __init(self):
        self.name = None
        self.date_birth = None
        self.general_registry = None
        self.ppr = None

    def print_name(self):
        return self.name


class Student:
    def __init__(self):
        self.registration = None
        self.grades = []

    def studying(self):
        return "studying..."


class Professor:
    def __init__(self):
        self.classes = []

    def teaching(self):
        return "teaching..."


student1 = Student()
professor1 = Professor()
