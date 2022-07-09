## this file will contain the 4-6 OOP Lesson
# Subclasses and inheritance
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

class Manager(Employee):
    raise_amount = 1.07
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer('Mark', 'Harmon', 50000, 'python')
dev_2 = Developer('Nick', 'Stick', 60000, 'js')
mg_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(issubclass(Manager, Developer))
print(isinstance(mg_1, Manager))
# mg_1.print_emp()
# mg_1.add_emp(dev_2)
# mg_1.print_emp()

# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)


# print(help(Developer))