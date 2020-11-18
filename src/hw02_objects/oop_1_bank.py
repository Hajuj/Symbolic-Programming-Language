"""Exercise 1: (5 points)

a) Using the slides & the script, put together a file containing the
   complete Account class.  Each method must have a documentation
   string at the beginning which describes what the method is doing.
   (1 point)

b) Create a main application where you create a number of accounts.
   Play around with depositing / withdrawing money.  Change the
   account holder of an account using a setter method.  (1 point)

c) Change the withdraw function such that the minimum balance allowed
   is -1000.  (1 point)

d) Write a function apply_interest(self) which applies an interest
   rate of 1.5% to the current balance and call it on your objects.
   (1 point)

e) Implement the __str__ magic method and use it to print accounts.
   (1 point)
"""
import re


class Account:
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
        initializing the class
        :param num: int (the personal number of the person)
        :param person: string (the name of the person/holder)
        """
        self.balance = 0
        self.number = num
        self.holder = person

    def deposit(self, amount):
        """
        Shows the balance after depositing cash to the bank account
        the balance was zero but when you deposit, it increases by the amount you deposit
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

    """because the balance decreases by the amount you withdrawn"""

    def print_info(self):
        """

        :return: Prints the current balance value
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


""" This is the main part of the program
    An object is being created as an example. First we assign the attributes and then 
    we can give different values to all the methods and functions we have created
    in our code. By different amounts of deposited and withdrawn money, the balance will be
    different in the end. With the setter method is also possible to change the name of the 
    account holder.
 """
if __name__ == "__main__":
    print("Welcome to the Python Bank!")
""" The objects 'a' and 'b' are being created with different attributes"""
a = Account(420, "IDK")
b = Account(999, "AnotherOne")
""" in the next code lines are being different values given 
    to the 'withdraw' and 'deposit' function, while also applying the interest"""
a.deposit(1200)
b.deposit(1800)
a.withdraw(300)
b.withdraw(420)
a.apply_interest()
b.apply_interest()
a.deposit(550)
a.deposit(870)
b.deposit(690)
b.withdraw(115)
a.withdraw(1280)
a.apply_interest()
b.apply_interest()

"""the first account holder's name is being changed from IDK to IDC
    and the second one from AnotherOne to SpecialOne"""
a.set_holder("IDC")
b.set_holder("SpecialOne")

print(a.__str__())
print(b.__str__())

