"""Exercise 1: (5 points)

a) Using the slides & the script, put together a file containing the
   complete Account class.  Each method must have a documentation
   string at the beginning which describes what the method is doing.
   (1 point)

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


class Account(object):
    """ This is a class that represents a bank account
    Attributes
    ----------
    num: int
         personal number of the person
    holder : String
             the name of the person

    Methods and functions
    ------
    deposit(self, amount): this method is used to show the balance after depositing cash to the bank account
    withdraw(self, amount): shows the amount that is about to be withdrawn
    set_holder(self, person): the setter method helps changing the account holder of an account
    get_holder(self): the getter method is used to complete the change made with the setter method
    __str__(self): this method is used to print accounts
    apply_interest(self): this is a function which applies an interest rate of 1.5%
                        to the current balance and call it on the given objects
    __str__(self): a method used to print accounts

     """

    def __init__(self, num, person):
        """


        :param num: int (the personal number of the person)
        :param person: string (the name of the person/holder)
        """
        self.balance = 0
        self.number = num
        self.holder = person

    def deposit(self, amount):
        """
        Shows the balance after depositing cash to the bank account

        :param amount: int
        :return: balance :: double
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Shows the amount that is about to be withdrawn

        :param amount: double
        :return: amount :: double
        """
        if self.balance - amount < -1000:
            amount = self.balance + 1000

        self.balance -= amount
        return amount

    def print_info(self):
        """

        :return: Prints the balance value as a string
        """
        print("Balance: ", self.balance)

    def set_holder(self, person):
        """
        the setter method helps changing the account holder of an account

        :param person: str : The name of the person
        :return: str
        """
        if (not type(person) == str):
            raise TypeError
        if not re.match("\w+( \w+)*", person.strip()):
            raise ValueError
        self.holder = person

    def get_holder(self):
        """
        The getter method is used to help the setter method
        """
        return self.holder

    def apply_interest(self):
        """
        A function which applies an interest
        rate of 1.5% to the current balance and call it on your objects.
        :return: double
        """
        self.balance *= 1.015

    def __str__(self):
        """
        a method used to print accounts

        :return: str
        """
        res = "***Account Info***\n Account ID: %i \n Holder: %s \n Balance: %i" % (
            self.number, self.holder, self.balance)

        return res


if __name__ == "__main__":
    print("Welcome to the Python Bank!")

