"""
Prime function : Discover if a number is prime
"""


def prime(number):
    if number > 1:
        for x in range(2, number):
            if (number % x) == 0:
                return "It's not a prime number"
        else:
            return "It's a prime number"
    else:
        return "It's not a prime number. Number less than or egual to 1"
