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

## Reading Data From Files:
#  #