## Modules ##
# Reusability is an important part of coding
# There are situations where we might opt to resuse a particular code rather
#       than develooping something from scratch ... enter modules
# 
# Modules refer to a file containing Python statements and definitions.
#   These are the pre-written codes that are written by someone else
#   which you can directly use in your code
# 
# We can define our most used functions in a module and import it, 
#   instead of copying their definitions into different programs
# 
#### Types of Modules: ####
#   Built-in Modules
#   Third-Party Modules
#   Custom Modules

# Built In Modules:
#   -are the modules built into python and maintained by the python dev team
#   -to use you can just import them and make the call to the methods you want
#       *EX: Math, Random, Time, Socket etc

# Third-Party Modules:
#   -only different here is we need to install them first (can be installed using pip)
#   - these modules are uploaded and stored at PyPI repo. The Python Package Index,
#           is the official software repo for Python
#       *Install CMD: 
#           windows - pip install module_name
#           mac/linux - pip3 install module_name

# Custom Modules:
#   -created by the dev(me) for reuse of code (need to service modules)

# How to use a Module:
#   import statement 1
#   import statement and renaming 2
#   the from ... import statement 3

# Import 1: import module_name (or for just a function from module: module_name.function())
# Import 2: import module_name as m (or m.function())
# Import 3: from module_name import functionName (if done with from you dont 
#               need to ref the module to use the funcition)
# EX #

#simple method
# import math
# math.factorial(5)

#rename method
# import math as mt
# mt.factorial(5)

#just the function
# from math import factorial
# factorial(5)

## Built In Modules:
# https://docs.python.org/3/py-modindex.html
# 
# Heres a few important ones:
# math - provides access to the mathmatical functions defined by C standard
#           https://docs.python.org/3/library/math.html
# random - implements pseudo random number generators for various distributions
#           https://doc.python.org/3/library/random.html
# statistics - provides for calculating math stats of numeric (real-valued data)
#           https://docs.python.org/3/library/statistics.html
# array - in python, we do not have a concept of arrays, but we can use the array module
#           which defines an object type that can compactly represent an array of basic
#           values. Arrays are constrained to one data type where lists are not
#           http://docs.python.org/3/library/array.html
# datetime - supplies classes for manipulating dates and time
#           http://docs.python.org/3/library/datetime.html
# time - provides various time related functions related to C time platform
#           https://docs.python.org/3/library/time.html
# sqlite3 - SQLite is a C library that provides a lightweight disk-based database
#           that doesn't require a separate sever process and allows accessing
#           the databasse,
#           https://docs.python.org/3/library/sqlite3.html
# urllib - a package that collects several modules for workin with URLs
#           https://docs.python.org/3/library/urllib.html
# tkinter - "TK Interface" standard TK GUI toolkit
#           https://docs/python.org/3/library/tkinter.html#module-tkinter


#### Working With Custom Modules: ####
# xX imported in the file_exceptions.py Xx #
# def add(num1,num2):
#     return num1+num2

# def sub(num1,num2):
#     return num1-num2

# def multiply(num1,num2):
#     return num1*num2

# def divide(num1,num2):
#     return num1/num2