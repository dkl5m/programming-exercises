"""
class Patient:
    pass
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
NAME MANGLING -> _Class__attribute
    used when you're testing your code
"""
