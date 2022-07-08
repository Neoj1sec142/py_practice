# OOP 1 of 6 - Classes and Instances
# Method - function associated with a class
# when using class variables the instance will always be searched first
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

emp_1 = Employee('Mark', 'Harmon', 50000)
emp_2 = Employee('Nick', 'Stick', 60000)

print(Employee.num_of_emps)

# print(emp_1.__dict__)
# print(emp_1.pay)

# print(emp_2.email)
# print(emp_1.email)

# Both of the below options achieve the same thing
# The class will need the instance passed in to know
# how to run the method requested
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.__dict__)
# emp_1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)