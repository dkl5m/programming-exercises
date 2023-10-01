# OBJECT AND ATTRIBUTE

class Account:

    # class attributes
    tax = 0.50

    """
    # decorator
    @classmethod
    def returnCode(cls):
        print("Code: 555")
    """

    @staticmethod
    def returnBancCode():
        return '345'

    # instance attributes
    def __init__(self, number, holder, balance=2000):
        self.number = number  # protected visibility
        self._holder = holder  # public visibility
        self.__balance = balance  # private visibility
        self.__historic = [balance]

    def balance(self):
        self.__balance -= Account.tax
        print(f'Statement: ${self.__balance}')

    def transaction(self, balance):
        self.__historic.append(balance)

    def bank_statement(self):
        print("----Bank Statement----")
        print("Account: ", self._holder)
        for balance in self.__historic:
            print(f'Bank statement: ${balance}')

    def deposit(self, value):
        self.__balance += value
        self.transaction(self.__balance)

    def withdrawal(self, value):
        self.__balance -= value
        self.transaction(self.__balance)

    def transfer(self, value, destiny):
        self.withdrawal(value)
        destiny.deposit(value)


"""
# Account class instances:
#      creates object that has the same data type as the class

account1 = Account(123, "John", 4000)
account2 = Account(456, "Elise", 5000)

print(account1.__dict__)
print(account2.__dict__)

account2.balance()

# Dynamic attribute -> created in execution time
account2.sign = 'Pisces'

print(account1.__dict__)
print(account2.__dict__)

del account2.sign

print(account2.__dict__)

# Self references the current value of the instances of my class,
# and must always be the first value to be written

# Class Method
# Convention
Account.returnCode()
account1.returnCode()

# Static Method

# Convention
# It will not receive a parameter that references the class itself
# Belongs to a class but doesn't have access to the class
print(Account.returnBankCode())
print(account1.returnBankCode())
"""

"""
COUPLING
Link between code units
can be strong or weak

VISIBILITY - modifier access

private - restrictive -> defines that attributes and methods can
only be manipulated within the class.

    Make the account attribute stronger: account -> __account (private)


protected - intermediary -> defines that attributes and methods
can only be manipulated within the class and classes that inherit
from the class where they were defined

    Make the number attribute stronger: number -> _number (protected)

public - less restrictive -> defines that attributes and methods
are accessible anywhere

Attributes has to start as private, and later, you change the visibility
Methods has to start as public

ENCAPSULATION - it helps on reuse and legibility of the code
ex:

Transfer to an account to another
    account1 = Account(123, 'Mona Lisa', 2300)
    account2 = Account(456, 'Albert', 2000)
    account1.withdrawal(300)
    account2.deposit(300)
    account1.extract()

We can encapsulate it in the function transfer

    def transfer(self, value, destiny):
        self.withdrawal(value)
        destiny.deposit(value)

And the holder will just make one step, that is use the transfer function
"""

account1 = Account(123, 'Mona', 2300)
account2 = Account(456, 'Albert')

account1.transfer(300, account2)
account1.balance()
account2.balance()
account1.transfer(456.50, account2)
account1.bank_statement()
