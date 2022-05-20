## FUNCTIONS ## 
#######################
# In simple words functions help us to groups tasks that only get
# executed when they are called -- a block of code that performs 
# a particular task and may accept optional user input and 
# accordingly give outputs
# 
# creating functions allows us to reuse the code later on without having
# to re create the function we can just call it instead
# 
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = num1+num2
# print("The sum is: ",num3)
# Functions SYNTAX:
# def DoSomething(param1, param2):
#   value = 1
#   return value
# 
# In python the def keyword is used to define a function
# The def keyword is followed by the name of the function and ()
# Keep your names smart
# () may contain the optional input paramters. a : marks the end of the fun header
# 
# Once the function header id defined, we can define the funciton body that may
# contian one or more Python statements -- indented
# return statments are option but return the value from function
# calling a funciton EX func_name()

# def sayHello();
#   print("hello world")

# def sayHello(name):
#     print("hello", name)
# sayHello("Neo")

# here we are passing sayHello the paramter name and printing it iin concatentated str
# functions dont require params but if they have them and we dont pass the funciton the 
# expected param when calling it it will result in a n error.
# 
# def addNum(nm1, nm2):
#     nm3 = nm1 + nm2
#     return nm3

# parameters are inside the functions ()
# arguements are passed to the function in respect to the params
# these values may come from user or based on caculations or processing
# 
# We can also pass a default value to our funcitons 

# def sayGello(name = 'GELLY'):
#     print("Hello",name)
# sayGello()

# and if the arguement is not passed it will rely on the default name
# 

# LAMBADA IN PYTHON #

#  #