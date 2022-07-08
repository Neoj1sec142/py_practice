## OOP - pt 3 of 6 - classmethods and staticmethods
# to add a method to a class add @classmethod above the method
class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Mark', 'Harmon', 50000)
emp_2 = Employee('Nick', 'Stick', 60000)

import datetime as dt
my_day = dt.date(2016, 7, 11) #= True
# my_day = dt.date(2016, 7, 10) #= False

print(Employee.is_workday(my_day))

# Employee.set_raise_amt(1.07)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
