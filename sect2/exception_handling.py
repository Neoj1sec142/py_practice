## EXCEPTION HANDLING ##
# As a user enters inforamtion to a db and say they leave a spot blank
#   this could arise DB Errors and possibly stop the program
#   Exception handling is the process of handling these errors to avoid that situtation
# Error Types:
#   Syntax Err - error in the source code of a program/also called compilion errors
#   Logic Err - undesirable actions caused by inproper logic in code
#   Runtime Err - means program complied correctly but when running leads 
#           to abnormal behavior or terminate the program
# Runtime Errors are generates when the program is runnning and lead to abnormal
#   behavoir or termination of the program -- such are called EXCEPIONS
# 
# Examples:
#   division by zero
#   accessing a file that does not exist
#   addition of two incompatible types
#   trying to access a nonexistent index of a sequence
#   removing the table fro the disconnected database server
# 
# Exception handling allows you ro separate error-handling from normal code
# an exception is a python object which represents and error
# allows you to simulate consequenses as the error handling takes place
#   in onw place and in one manner
# an exception is a convenient method for handling err messages
# 
# Python Exceptions:
# An exception class in python is the base class form which exceptions inherit.
# this means, all the common built-in exceptions inherity from this class
# 
# -StandardError - is the base class for all built-in exceptions except StopIteration and SystemExit
# -ArithmeticError - is the base class for all error that occur for numeric calculation
# -FloatingPointError - is raised when a floating-point calculation fails
# -ZeroDivisionError - is raise when a division or modulo by zero takes place for all numeric types
# -EOFError - is raised when there is no input from the input() funciton and the end of the file is reached
# -ImportError - is raise when an import statment fails
# -KeyboardInterrupt - is raise when the user interrupts the program execution ususal Ctrl + C
# -IndexError - is raised when and index is not found in a sequence
# -NameError - is raise when an identifier is not found in the local or global namespace
# -IOError - is raised when an input/output operation fails, such as the print statement
#       or the open() funciton when trying to open a file that doesnt exist
# -SyntaxError - is raised when there is an error in Python syntax
# -IndentationError - is raise when indentation is not specified properly
# -TypeError - is raise when an operation or funciton is attempted that is invaild for the specified data type
# -ValueError - is raise when the buiult-in funcituon for a dta type has the valid type of argument, but the
#           argument have invalid values specified

# Exception Handling Structure:
# Python has two following statements that help us to handle and work with exceptions
#   Try Statement
#   Except Statement(Kind of like a catch)

# EX:
# try:
    #statements that can raise the error
# except Exception1:
    #if there is Exception1 this block will execute
# except Exception2:
    #if there is Exception2 this block will execute

# A single try block can have multiple exceptblocks. Thus if the try throws
#       multiple exceptions they are handled resepectively
# You can also provide a generic except clause, which handle any exception.
#       here we can use the exception class
# Also after the except clause you can include an else-clause. The code in 
#       the else block executes if the code in try does not raise any exception
# 
# try:
#     print(name)
# except NameError:
#     print("Some err occured. Please contact the dev")

# Or we can eve send the err with message

# try:
#     print(name)
# except NameError as e:
#     print("An err occured please contact the dev", e)
# try:
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number:"))
#     print("Division is:", num1/num2)
# except Exception as e:
#     print("Oops you cannot divide a number by zero")

# try:
#     fp = open('thisdoesnt.txt', 'r')
#     print(fp.read())
#     print(fp.close())
# except Exception as e:
#     print("Oops, looks like this file doesn't exist", e)

# try:
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number:"))
#     print("Division is:", num1/num2)
#     print("Thank you for choosing our calculator")
# except Exception as e:
#     print("Oops you cannot divide a number by zero")
# finally:
#     print("Thank you for using our calculator")

# Here you can see that the thank you statement is not executed if the 
    # exception is raised in the division line therefore we can assume that 
    # inside the try block if an err is thrown the following code will not
    # execute and it will differ to the except statement
# Sometimes we still need to execute something after the excption though(Finally)

# Raise Exceptions:
# You can also manually raise an exception yourself using the raise keyword
# syntax: raise Exception("message")
# Exception is the type of exception(ex NameError)
# the arguement message is a value for the exception(optoional)
# EX #
# try:
#     a = int(input("Enter a positive integer:"))
#     if a <= 0:
#         raise ValueError("It is not a positive number")
# except ValueError as e:
#     print(e)