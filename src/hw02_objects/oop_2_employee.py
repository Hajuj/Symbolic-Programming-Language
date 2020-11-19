"""Exercise 2: (5 points)

a) Write the complete code for the Employee class (including
   constructor, __str__, ...). (2 points)

b) Create a main application, create a few employee objects and show
   how you can manipulate them using the methods. (1 point)

c) Create a department dictionary (dictionary of strings to lists/sets
   of employees) with at least two departments (e.g. "accounting",
   "sales", ...) with each at least two employees. Print for each
   employee in the dictionary "<department> <employee name>".
   (2 points)

"""
import re


class Employee:
    # Constructor
    def __init__(self, num, person):
        self.balance = 0
        self.number = num
        self.holder = person

    # Methods
    def withdraw(self, amount):
        if amount > self.balance:
            amount = self.balance
        self.balance -= amount
        return amount

    def deposit(self, amount):
        self.balance += amount

    def print_info(self):
        print("Balance:", self.balance)

    def set_holder(self, person):
        if (not type(person) == str):
            raise TypeError
        if not re.match("\w+( \w+)*", person.strip()):
            raise ValueError
        self.holder = person

    def get_holder(self):
        return self.holder

    # String representation
    def __str__(self):
        return f"Employee application\n" \
               f"Employee ID: {self.number}\n" \
               f"Employee name: {self.holder}\n" \
               f"Balance: {self.balance}\n"


# Main part of the program
if __name__ == "__main__":
    # Creating Objects & assigning attributes
    hjjEmp = Employee(69, "HJJ")
    hjjEmp.deposit(500)
    hjjEmp.withdraw(200)
    hjjEmp.set_holder("bro")
    shadyEmp = Employee(420, "Shady")
    shadyEmp.deposit(600)
    shadyEmp.withdraw(400)
    shadyEmp.set_holder("idk")
    # Accessing attributes
    print(hjjEmp)
    print(shadyEmp)

# Dictionary
dep = {
    "dep1": "Accounting",
    "dep2": "Sales"
}
emp = {
    "emp1": "HJJ",
    "emp2": "Shady",
    "emp3": "Rajna",
    "emp4": "Naira"
}
print(dep["dep1"] + " " + emp["emp1"] + "\n" + dep["dep1"] + " " + emp["emp2"])
print(dep["dep2"] + " " + emp["emp3"] + "\n" + dep["dep2"] + " " + emp["emp4"])
