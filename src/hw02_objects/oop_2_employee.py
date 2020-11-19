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
    """gives the number of employees as result"""
    count_employees = 0

    # Constructor
    def __init__(self, firstName, lastName, personalNumber, workingHours, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.personalNumber = personalNumber
        self.workingHours = workingHours
        self.salary = salary
        Employee.count_employees += 1

    # prints information about the number of employees in the company
    @staticmethod
    def employees_info():
        print("Total number of employees in our company is: %d " % Employee.count_employees)

    # string representation of the employees
    def __str__(self):
        info = "*Employee Info* \n"
        info += "First Name is: " + self.firstName + ".\n"
        info += "Last Name is: " + self.lastName + ".\n"
        info += "ID Number is: " + str(self.personalNumber) + ".\n"
        info += "This employee has worked: " + str(self.workingHours) + " hours.\n"
        info += "The salary of this employee: " + str(self.salary) + "\n"
        return info

    # Setting a new ID Number
    def set_idnumber(self, new_idnumber):
        self.personalNumber = new_idnumber

    def get_idnumber(self):
        return self.personalNumber

    # Setting new amount of working hours
    def set_workinghours(self, hours):
        self.workingHours = hours


"""Main part of the program
Creating employee objects and assigning attributes
First is being shown the Information of each employee and then are
some of the information is being changed, using methods
"""

if __name__ == "__main__":
    print("Employee application \n")
    employee1 = Employee("Rajna", "Fani", 666, 60, 1200)
    employee2 = Employee("Shady", "Mansour", 777, 65, 1300)
    employee3 = Employee("Hajuj", "Hazhuzh", 888, 62.5, 1250)

# changing the personal number and the amount of working hours for employee1
    print(employee1)
    print ("After some changes: ")
    employee1.set_idnumber(888)
    employee1.set_workinghours(65)
    print(employee1)

# changing the amount of working hours for employee2
    print(employee2)
    print ("After some changes: ")
    employee2.set_workinghours(60)
    print(employee2)

# changing the personal number for employee3
    print(employee3)
    print ("After some changes: ")
    employee3.set_idnumber(666)
    print(employee3)

# Creating a dictionary with two different departments
dep = {
    "dep1": "Accounting",
    "dep2": "Sales"
}
# the employees in each department
emp = {
    "emp1": "HJJ",
    "emp2": "Shady",
    "emp3": "Rajna",
    "emp4": "Naira"
}

print(dep["dep1"] + ": " + emp["emp1"] + "\n" + dep["dep1"] + ": " + emp["emp2"])
print(dep["dep2"] + ": " + emp["emp3"] + "\n" + dep["dep2"] + ": " + emp["emp4"])
