"""Exercise 1: (5 points)

a) Using the slides & the script, put together a file containing the
   complete Account class.  Each method must have a documentation
   string at the beginning which describes what the method is doing.
   (1 point) TODO

b) Create a main application where you create a number of accounts.
   Play around with depositing / withdrawing money.  Change the
   account holder of an account using a setter method.  (1 point)  TODO

c) Change the withdraw function such that the minimum balance allowed
   is -1000.  (1 point)

d) Write a function apply_interest(self) which applies an interest
   rate of 1.5% to the current balance and call it on your objects.
   (1 point) TODO(APPLY ON OBJECT)

e) Implement the __str__ magic method and use it to print accounts.
   (1 point)
"""
import re


class Account:
    """ Here has to be a documentation string that describes
    which data objects this class is designed for.
    You have to remove the pass statement and then write some
    code for the class. """

    def __init__(self, num, person):
        self.balance = 0
        self.number = num
        self.holder = person

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < -1000:
            amount = self.balance + 1000

        self.balance -= amount
        return amount

    def print_info(self):
        print("Balance: ", self.balance)

    def set_holder(self, person):
        if (not type(person) == str):
            raise TypeError
        if not re.match("\w+( \w+)*", person.strip()):
            raise ValueError
        self.holder = person

    def get_holder(self):
        return self.holder

    def apply_interest(self):
        self.balance *= 1.015

    def __str__(self):
        res = "***Account Info***\n Account ID: %i \n Holder: %s \n Balance: %i" % (
            self.number, self.holder, self.balance)

        return res


if __name__ == "__main__":
    print("Welcome to the Python Bank!")
