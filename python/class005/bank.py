# OBJECT AND ATTRIBUTE

class Account:

    # class attributes
    tax = 0.50

    # decorator
    @classmethod
    def returnCode(cls):
        print("Code: 555")

    @staticmethod
    def returnBancCode():
        return '345'

    # instance attributes
    def __init__(self, number, holder, balance):
        self.number = number
        self.holder = holder
        self.balance = balance

    def statement(self):
        self.balance -= Account.tax
        print(f'Statement: ${self.balance}')

    def deposit(self, value):
        self.balance += value

    def withdrawal(self, value):
        self.balance -= value


# Account class instances:
#      creates object that has the same data type as the class

account1 = Account(123, "John", 4000)
account2 = Account(456, "Elise", 5000)

print(account1.__dict__)
print(account2.__dict__)

account2.statement()

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
print(Account.returnBankCode())
print(account1.returnBankCode())
