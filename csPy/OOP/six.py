# Property Decorators - Getters, Setters, and Deleters - OOP pt 6
from contextlib import nullcontext


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print("name deleted")
        self.first = None
        self.last = None
    

emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Joe Shmoe'

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
