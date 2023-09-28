__doc__ = """
This module returns if a number is prime or not

available functions:
    prime
"""
# put in terminal "print(prime.__doc__) to see the docs"
# or help(prime) --> return all dunder objects


def prime(number):
    """
    This function returns if a number is prime or not
    prime(parameter) -> the parameter must be an integer
"""

    if number > 1:
        for x in range(2, number):
            if (number % x) == 0:
                return "It's not a prime number"
        else:
            return "It's a prime number"
    else:
        return "It's not a prime number. Number less than or egual to 1"


if __name__ == '__main__':
    print("Prime module Hello")
