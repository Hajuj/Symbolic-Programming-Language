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


class Employee:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # Methods
    def money_lost(self, amount):
        self.money -= amount

    def money_won(self, amount):
        self.money += amount

    def __str__(self):
        return f"Employee name: {self.name}\n" \
               f"New balance: {self.money}\n"


if __name__ == "__main__":
    # Creating Objects & assigning attributes
    emp1 = Employee("HJJ", 69)
    emp1.money_won(500)
    emp1.money_lost(200)
    emp2 = Employee("Shady", 20)
    emp2.money_won(600)
    emp2.money_lost(200)
    # Accessing attributes
    print("Employee application")
    print(emp1)
    print(emp2)

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
