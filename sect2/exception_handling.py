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
#  #