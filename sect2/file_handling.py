## FILE HANDLING ##
#############################
# Files are named locations on a disk to store related info
# They are used to permanently store data in a non-volatile
#   memory such as hard diskd and more
# 
# These files can be .csv .txt and more
# 
# In simple words a file is a named location to store information
# One can just flush data into files such as .csv .txt .docx etc
# 
# Opening Files:
# open() funciton is a built in way to open files creating a file object 
# syntax:
# file_object = open(file_name, access_mode)
#   file_name - is the name of the file with extension. we can also add the absolute path
#   access_mode - it defines the mode in which the file has been opened. 
# 
# Access Modes:
#   Read Mode:
        # r -opens a file in readonly mode file pointer is placed at the beginning of the file
        # rb - opens a file for reading only in binary format
        # r+ - opens a file for both reading and writing
        # rb+ - opens a file for both reading and writing in binary format #
#   Write Mode:
        # w - opens a file in write-only mode, it will overwrite the file if the file exists.
        #           if no file exists it will creat a new one
        # wb - opens a file for write only in binary
        # w+ - opens a file for both reading and writing
        # wb+ - opens a file for reading and writing in binary format
#   Append Mode:
       # a - opens a file for appending and adds the appendage at the end
       # ab - opens a file for appending in binary format
       # a+ - opens the file for appending and reading
       # ab+ - opens the file for appending and reading in binary format
## below is the correct syntax for opening a file
# fp = open('python.txt', 'r')

# Python has a few built in methods to read the content of the file.
# read() - reads a string from an open file. It read the content until it reaches the end of the file
# read(size) - accepts a param as size, the passed param is the num of bytes to be read from the opened file
#                this method starts reading from the beginning of the file until the num of byte specified
# readline() - It reads on single line of the file at a time
# readline() - It reads all the lines until it reaches the end of the file
# fp = open('python.txt', 'r')
# print(fp.read(6)) #= Python
# print(fp.readline()) #= Python is a general-purpose, high-level, object-oriented programming language.

## Writing Data To Files:
# fp = open('python.txt', 'a')
# Pythons built in methods for writing to doc
# write() - writes any string to an open writable file
# syntax : file_object.write(data)
# fp.write("\npython is a really cool language")
# after running the code if you check out the python.txt file the file has actually been overwritten

# CLOSING A FILE:
# as with DBs we need to close them after to free the provisional usage of RAM 
# syntax : file_object.close() 
# fp = open('python.txt', 'r')
# print(fp.read())
# fp.close()

# Manipulating File Pointers
# 
# The file pointer is basically the cursor that represents the position where it is in the file.
# When working w/files the pointer is at the beginning when we start reading or writeing to a file
# While appending, the file pointer is at the end of the file
# 
# Methods:
# tell() - method tells you the current position of the pointer within the file
# seek(position, from) - changes the current file position. 
#       The position arguement indicates the number of bytes to be moved.
#       The 'from' argument(optional) specifies the reference position fro where the byte are moved
# fp = open('python.txt', 'r')
# print("Pointer position  before reading is:", fp.tell()) #= 0
# print(fp.read())
# print("Pointer position after reading is:", fp.tell()) #= 54
# fp.seek(5)
# fp.close()
#  #