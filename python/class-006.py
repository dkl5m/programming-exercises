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
