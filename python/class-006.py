# FUNCTIONS

"""
# Imperative paradigm
# imperare = command

# features = variables, attributions and mostly sequential
# C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

# Extern block
name = "Hugh"  # global var


def my_function():
    # Intern block
    # function intern block is known as function body
    name = "Halle"  # local var
    tuple1 = 2, 5, 6, 7, 8, 9
    print(name)
    print(tuple1)
    if name == "Halle":
        print("if condition intern block printing")


my_function()
print(name)
"""

# FUNCTION RETURN
"""
list1 = [1, 2, 3, 4, 5]
print(list1)

return1 = list1.pop()
var1 = print("Hello World")
print(list1)
print("Pop function return: ", return1)  # return popped value
print("Print function return: ", var1)  # return nothing


def hello_world():
    return "Hello World!"


print(hello_world())


def even_odd():
    pass  # if you're working and want to test the code with a function not
    # finished, use pass to make the error desapear
    # pass is used for python not to crash your code, on the first error


even_odd()


def even_odd1():
    number = 4
    if (number % 2) == 0:
        return "even number"
        # In the first return, python will leave the function
    return "odd number"


print(even_odd1())
"""

# INFINITE LOOP = ERROR
"""

def hello_world():
    print("Hello World")


def execute():
    hello_world()


execute()
"""

# FUNCTION PARAMETERS


def my_function():
    var = "Maria"
    return var


print(my_function())
var = "Ana"
var1 = my_function()
print(var)
print(var1)


def function_name(parameter):  # parameter is the name given to the
    # values used in the definition of the function
    # body of function
    print("Hello", parameter)


name = input("What is your name?")
function_name(name)  # argument is the name given to the values
# used in the function call


def print_name(name1, surname1):
    print(f"Hello, {name1} {surname1}")


name1 = input("What is your name?")
surname1 = input("What is your surname?")
function_name(name1, surname1)
