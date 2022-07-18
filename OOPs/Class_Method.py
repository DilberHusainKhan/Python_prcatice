class Employee:
    increment = 1.5
# Constructor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# method
    def increments(self):
        # self first search increment in instance then in class
        # or we can use Employee.increment
        # self.salary = int(self.salary * self.increment)
        self.salary = int(self.salary * Employee.increment)


# object
dilber = Employee("Dilber Husain Khan", 40000)

# print
print(dilber.salary)
dilber.increments()
print(dilber.salary)

# to check all the varaible of instance use --- __dict__
print(dilber.__dict__)
