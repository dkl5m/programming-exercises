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

"""
class Person:

    # (superclass) - Parent class

    def __init__(self, name=None, date=None, general_registry=None, ppr=None):
        self.name = name
        self.date_birth = date
        self.general_registry = general_registry
        self.ppr = ppr
        print("Class Person")

    def print_name(self):
        return self.name


class Student(Person):

    # (subclass) - Child class

    def __init__(self, name):
        super().__init__(name)
        self.registration = None
        self.grades = []
        print("Class Student")

    def studying(self):
        return "studying..."


class Professor(Person):
    def __init__(self, name):
        super().__int__(name)
        self.classes = []

    def teaching(self):
        return "teaching..."


student1 = Student('Ana')
print(student1.print_name())

professor1 = Professor('Karine')
print(professor1.print_name())

print(student1.studying())
print(professor1.teaching())
"""
"""
print(type(student1))
print(type(professor1))
"""

# POLYMORPHISM

"""
Polymorphism just exists if heritage exists
It is not necessary to apply
each object will shape the way to execute the same method

"""


class Person:

    def __init__(self, name=None, date=None, general_registry=None, ppr=None):
        self.name = name
        self.birth_date = date
        self.general_registry = general_registry
        self.ppr = ppr

    def print_name(self):
        return self.name

    def work(self):
        print("working...")


class Admin(Person):
    pass


class Professor(Person):

    def __init__(self, name):
        super().__init__(name)
        self.classes = []

    def work(self):
        class_name = self.__class__.__name__
        print(f"Class {class_name} Teaching...")


class Student(Person):

    def __init__(self, name):
        super().__init__(name)
        self.registration = None
        self.grades = []
        print("Class Student")

    def studying(self):
        return "studying..."


professor1 = Professor('Rambo')
admin1 = Admin()
professor1.work()
admin1.work()
