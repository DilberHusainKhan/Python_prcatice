class Employee:
    no_of_Employee = 0
    increment = 1.5
# Constructor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.no_of_Employee += 1

# normal method or function me instance pass hota hai as an argument
    def increments(self):
        # self first search increment in instance then in class
        # or we can use Employee.increment
        self.salary = int(self.salary * self.increment)
        # self.salary = int(self.salary * Employee.increment)
# class method me decorator lagta hai @classmethod or class pass hota hai as an argument

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


print("No of Employee ", Employee.no_of_Employee)
# object
dilber = Employee("Dilber Husain Khan", 40000)
Humayun = Employee("Humayun Khan", 60000)
Imdad = Employee("Imdad Husain Khan", 20000)

# print
print("No of Employee ", Employee.no_of_Employee)
print(dilber.salary)
Employee.change_increment(4)
dilber.increments()
print(dilber.salary)

# to check all the varaible of instance use --- __dict__
print(dilber.__dict__)
