# TUPLES
##################################
# Similar to lists tuples allow is to store multiple values in a single variable
# Lists = mutable(able to be changed) Tuples = immutable(not able to change-Read Only)
#   tuples are odered collections o multiple values
#   are immutable, and are read only not changable or manipulateable
#   also allow us to store duplicate values
# Tuple = () List = []
# can have any number of items and can be different types(int,float,str)
# tup1 = ()
# tup2 = (1,4,6,3,9)
# tup3 = ("John", 23,56.3,True)
# print(tup3) #= ('John', 23, 56.3, True)

# Manipulating Tuples:
# languages = ("Python", "Java", "Ruby", "Lisp")
# print(languages[1]) #= Java accessing
# print(languages[1:4]) #= ('Java', 'Ruby', 'Lisp') slicing
# since tuples are immutable we cant delete items inside
# we can however delete the entire tuple
# tupl1 = (12,56,98)
# print(tupl1)
# del tupl1

# Basic Operations on Tuples:
# One thing to keep in mind when using operations on tuples is that they are
# not like lists, since they are immutable any operations will always 
# return a new tuple

# tup1 = (1,2,3)
# tup2 = (4,5,6)
# print(tup1+tup2) #= (1, 2, 3, 4, 5, 6) concatentation
# print(tup1*3) #= (1, 2, 3, 1, 2, 3, 1, 2, 3) repetition
# print(2 in tup1) #= True membership

# For loop tuple iteration:
# cities = ("London", "Tokyo", "New York")
# for city in cities: 
#     print(city)

# Built in functions for tuples:
# len(tuple) - returns the length of the tuples
# min(tuple) - return the elements of the tuples with the minimum value
# max(tuple) - return the elements of the tuples with the maximum value
# nums = (3,56,78,13,98,33)
# print(len(nums)) #= 6
# print(min(nums)) #= 3
# print(max(nums)) #= 98

# Tuple Methods:
#   since tuples are immutable we only have a few tuple methods
# index(element) - returns the index of the first mathced item
# count(element) - returns the count of how many times the passed ele occurs
# exam = (23,45,23,67,89,1)
# print(exam.count(23)) #= 2
# print(exam.index(67)) #= 3

### Why Tuples? ###

# We generally use tuples for heterogeneous(different) data types
# and lists for homogeneous(similar) data types
# 
# Since tuples are immutable, iterating though a tuple is faster than a list.
#  so there is a slight performace boost
# 
# Tuples that contain immutable elements can be used as a key for a dictionary
# (Dictionarys = Objects in JS)
# 
# If you have data that doesn't change, implementing it as a tuple
#  will guarentee that is remains write-protected
