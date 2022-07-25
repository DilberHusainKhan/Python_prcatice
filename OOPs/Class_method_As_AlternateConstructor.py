class Employee:
    amount = 1.3

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increse(self):
        self.salary = self.salary*self.amount

    @classmethod
    def change_increment(cls, amount):
        cls.amount = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)


Dilber = Employee('Dilber', 'Husain', 76000)
humayun = Employee.from_str("Humayun-Anwar-75000")

print(humayun.salary)
print(Dilber.fname)
