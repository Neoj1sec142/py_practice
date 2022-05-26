## Object Oriented Programming (OOP) ##

# In the subject "Getting Started" we defined Python
#   as a general-purpose, high-level, object-oriented
#   programming language...
# 
# OOP:
# In programming, there are different paradigms or 
#   patterns that define how to write and structure our code.
#   Also, each paradigm has different functionalicties and behaviors
# EX of vairous programming patterns:
#   Structural programming
#   Procedural Programming
#   OOP
#   Functional Programming
#   etc
# 
# OOP is a programming paradigm that provides a means 
#   for structuring programs so that properties and behaviors
#   are bundled into individual objects
# In the initial subjects, we have seen that the type() method
#   in Python return the type of object i.e the data type of 
#   variable

#   EX: 
# name = "John"
# print(type(name))

# Here focus on the word, 'class'. The variable 'name' belongs 
#   to something called <class 'string'>
# 
# Classes and Objects INTRO:
# OOP is a programming paradigm that provides a means for structuring
#   programs so that properties and behaviors are bundled into 
#   individual objects
# We can say the object of the class 'string' at the most basic lvl
# OOPs in Python is a programming approach that focuses on using 
#   objects and classes as the building blocks of the programs
# It allows devs to develop apps using OOPs approach with a major focus
#   on code reusablility
# In simple words OOP is an approach for modeling concrete, real-world
#   thing, and relations between those things
# OOP models real-world entities as programming objects that have 
#   some data associated with them and can perform certain functions
# 
# Principles: (the 4 pillars of OOP)
# ############
# Abstraction - means to abstract only the details/data which migh concern the user
#       EX: phone apps show buttons but dont show how they function
# Encapsulation - similarly we try to encapsulate all the data as a single entity
#       EX: like a tunnel input in one way output comes out the otherside(what happens inside is hidden)
# Inheritance -one element can inherit various capabilities from another element
        # here the element we are referring to is a 'class' 
        # inheritance supports the concept of reusability
        # when we want to create some feature and there is already such
        #   a feature that includes some of the code that we want, then we 
        #   can derive our feature from the existing one instead of developing from scratch
# Polymorphism - means having many forms(poly = many, morphism = forms)
        # we can define polymorphism as the ability of something to have 
        #   more than one form.
        # Consider a geometric shape. As a whole, its termed as a shape,
        #   but that shape can have many forms such as triangle circle, square
        #   rectangle, oval , etc
        # Similarly in programming an operation may exhibit different
        #    behaviors in different instances
        # These behaviors depend upon the types of data used in the operation
# 
# Classes and Objects:
# Of the 4 pilliars the Classes and Objects are the building clocks of the 
#   object oriented system
# These pillars and building blocks combined make an object-oriented program
#   which is altogether a complete programming paradigm
# 
# Classes:
# - Just like lists, tuples, dictonaries...classes are some advaced data structures
#       to store manipulate, and structure the data
# - Data structures like lists, tuples and dictionaries can group and store only
#       a few attributes, but a class is a type of user defined stucture that can 
#       store various attirbutes
# - (Data - both primitive and user-defined) along with their functionalities,
#       all together as a single unit
# - These attributes and their fictionalies(behaviors) can be accessed via Objects
# - A class is a user-defined prototype for and object the defines the set of attributes that 
#       characterize and object of that class.
# - In simple words, a class is just like a prototype depending on which the real-world
#       objects are created
# - Basically a a class is a blueprint to create objects
# 
# Objects:
# - Objects are called as an instance of the class. as we have seen, a class is just
#       a blueprint, so a description of the object to be created
# - According to the class the object will be created with real data(input form creating 
#       a user with preset keys)
# - In Python a object has 2 values:
#       Attributes(Data variables of the class)(ex: user and stats)
#       Behaviors(Functions defined in the class)(ex: attacks and moves)
# 
# Working with Classes and Objects:
# SYNTAX of Class: class className:
# -class is the keyword used to define the class in Python
# - className is the name given to the class. Just like a name of a variable or 
#       function is should be meaningful
# - finally it is terminated by a semi colon 
# - inside the class we can define the attibutes and functions and the body of 
#       the class which should be indeneted #

# class Employee:
#     pass 
# the pass keyword suggests it does nothing. It is ignored by the interpreter but
        #is used as a placeholder or is an element is to be fullfilled without assigning operations

# class Employee:
#     empName = 'John'
#     age = 35
#     designation = "Manager"
# Since a class is a description and an object is an instance with that description
# -When we declare an object an object of the class, at that time the memory is allocated
#       to it and then we can access the attibutes and methods of the class
# STYNTAX used to define an object of a class
# objName = className()
# - we can declare an object by giving it a name followed by the assignment operator
#        with the className ending with parentheses
# - once delcared we can acces the attibuted and mmethods using the following syntax:
# objName.attributeName
# objName.methodName() #

# class Employee:
#     empName = 'John'
#     age = 35
#     designation = "Manager"

# empOne = Employee()
# print(empOne.empName) #= John

# We know that each object is a unique instance of the class and each
#        object has its own attribute and behavoirs
# This is obviously not preducutive as it is already defined we will get to constuctors next

# Constructor and Self:
# - constuctors are generally used for instantiating an object
# - the task of constructors is to inialize(assign values) the data members of the class when
#       an object of the class is created
# SYNTAXof constructor: def __init__(self):
# - the attributes that all objects must have are define in a dunder method called __init__()
# - everytime a new object is created __init__() sets the initial state of the object
#       by assigning the values of the objects properties
# Two Types of Contructors:
# - Default Constructor: is the constructor that doesn't accept any arguements.
#       is definition has only one arguement(self) which is a reference to the instance 
#       being constructed
# - Parameterized constructor: is a constuctor with parameters. It takes its first arguement 
#       as a refernce to the instance being constucted known as self and the rest of the 
#       arguements are provided.
#       These are the required attributes for the class
# *****Note: when your class has a default constructor, you can create the object using
# SYNTAX def constructor: objName = className() 
# - also if you do not provide any constuctor Python automatically assigns a defualt 
#       cosntructor to the class
# - if your class has a parameterized constructor, then when you create an object, 
#       you will need to pass those required numbers of arguements just like we do when we 
#       have a function that accepts a parameter
# SYNTAX for param constructor: objName = className(param1,param2,param3) #
# class Employee:
#     def __init__(self):
#         self.empName = 'John'
#         self.age = 35
#         self.designation = 'Manager'



# class Employee:
#     def __init__(self, empName, age, designation):
#         self.empName = empName
#         self.age = age
#         self.designation = designation

# empOne = Employee("John", 35, 'Manager')
# empTwo = Employee("Nick", 27, "Developer")
# print(empOne.empName)
# print(empTwo.empName)

# In OOP ithe self keyord works like a label and helps the class to
#    individuall recognize the instance(object) and accordingly pass data to the object
# When multiple objects of a class are created the self kjeyword helps the vlass to know which 
#       object is requesting to access the attribute and the methods and depending upon the 
#       object parameters the data is processed
# 
# Adding Behaviors:
# - when we define functions inside a class, they are consodered methods
# class Employee:
#         totalEmployees = 0
#         def __init__(self, empName, age, designation, salary):
#                 self.empName = empName
#                 self.age = age
#                 self.designation = designation
#                 self.salary = salary
#                 Employee.totalEmployees = Employee.totalEmployees + 1
#         def getEmpDetails(self):
#                 return self.empName, self.age, self.designation, self.salary
#         def updateSalary(self, newSalary):
#                 self.salary = newSalary
#                 print('Salary Updated')
#                 return self.salary
# as you can see totalEmployees is noot defined inside the __init__ method, 
#       and also it is not passed in the constructor
# this is becayse that value has to be calculated by the program and should not
#       be passed at the time of object creation
# so when a new employee is created we update that value by =1
# since we are not passing it we do not use self to refer to it and instead use
#       the class name : Employee.totalEmployees
# such variables that are shared by all the instances(objects) are called Class variables,
#       And the variables that are defined inside __init__ are called Instance variables
# Here we created the def getEmpDetails, and updateSlary:
# the getEmpDetails() simply returns all the details about eh employee
# the updateSalary() method accepts a parameter as newSalary and updates the 
#       self.salary to the passed value
# Every method in a class has a default paramter as self #
# empOne = Employee('John', 35, 'Mnager', '35000')
# print(empOne.getEmpDetails())
# empTwo = Employee('Sam', 26, 'Python Dev', 27000)
# print(empTwo.getEmpDetails())

# empOne.updateSalary(40000)
# empTwo.updateSalary(175000)
# print(empTwo.getEmpDetails())
# print(Employee.totalEmployees)

# Inheritance is when one class inherits various characteristics and capabilities from another class
#       here the characteristics we are talkin about are the attributes of yhe class, while the capabilities
#       are its behavior(methods of the class)
# Parent Class: is the class being inherited from the other classes. It is also called the Base Class
# Child Class: is the class that inherits from another, also called a Derived Class
# SYNTAX of inheritance
# class BaseClass:
        # body of base class
#       class DerivedClass(BaseClass):
#               #body of derived class
# 
# as you can see we can pass the name of the base to the derived class in parentheses
# class Employee:
#         totalEmployees = 0
#         def __init__(self, empName, age, designation, salary):
#                 self.empName = empName
#                 self.age = age
#                 self.designation = designation
#                 self.salary = salary
#                 Employee.totalEmployees = Employee.totalEmployees + 1
#         def getEmpDetails(self):
#                 return self.empName, self.age, self.designation, self.salary
#         def updateSalary(self, newSalary):
#                 self.salary = newSalary
#                 print('Salary Updated')
#                 return self.salary
# class Intern(Employee):
#         pass
# whenever we create an object of the child class and try to access it, it will first search
#       for that in the child class, if found it will execute it and return the data. If
#       not found, then it will search and access the data from the parent class #
# internOne = Intern('Tom', 22, 'Marketing', 12000)
# print(internOne.getEmpDetails())       