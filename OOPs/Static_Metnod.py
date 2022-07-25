class Employee:
    amount = 1.5
    # constructor

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary *= self.amount

    @classmethod
    def increment_amount(cls, amount):
        cls.amount = amount

# we can call static method without making object
    @staticmethod
    def isOpen(day):
        if day == 'sunday':
            return False
        else:
            return True


print(Employee.isOpen("monday"))
