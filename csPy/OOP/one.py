# OOP 1 of 6 - Classes and Instances
# Method - function associated with a class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Mark', 'Harmon', 50000)
emp_2 = Employee('Nick', 'Stick', 60000)

# emp_1.first = 'Mark'
# emp_1.last = 'Harmon'
# emp_1.email = 'neib1503@icloud.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Nick'
# emp_2.last = 'Stick'
# emp_2.email = 'nsjhdshvcj@icloud.com'
# emp_2.pay = 40000

# print(emp_2.email)
# print(emp_1.email)

# Both of the below options achieve the same thing
# The class will need the instance passed in to know
# how to run the method requested
print(emp_1.fullname())
print(Employee.fullname(emp_1))

