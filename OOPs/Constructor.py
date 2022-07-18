# concept of constructor
# pass  ---> means noting

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


dilber = Employee("Dilber Husain Khan", 23, 45000)
humayun = Employee("Humayun Anwar Khan", 24, 60000)

print(
    "Your name is", dilber.name, ", Your age ", dilber.age, ", and Your salary is ", dilber.salary)
print(
    "Your name is ", humayun.name, "Your age", humayun.age, "and Your salary is", humayun.salary)
