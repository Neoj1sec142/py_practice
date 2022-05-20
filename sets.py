### SETS ###
#####################
# python provides a builtin set type, sets are distinguished from other object
#   types by the unique operations that can be performed on them
# sets are unordered collections, there is no index attached to any
#   element in a python set.
# set elements are unique. this means duplicate elements are NOT allowed
# a se itself can be modified, but the elements contained in the set must be 
# immutable type
# 
# a set is created using the set() function or placing all the elements in {}
# thing to note** dictionaries use {} but have KVP thus ...
# {} is an empty dictionary not an empty set
# an empty set can be created as below function

# data = set()
# print(type(data))

# sets can't have lists or dictionaries in it, since we know, sets are mutable but 
# the sset elements have to immutable
# a valid set can have values of numeric,str,tuple,boolean data types

# setOne = {1,2,3}
# setTwo = {6,7,8, "james"}
# print(setOne) #= {1, 2, 3}
# print(setTwo) #= {8, 'james', 6, 7}

# since the data types of sets are unordered we have to loop through to access
# days = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
# print(days)
# for day in days: 
#     print(day)

# Sets Operations:
# EX of (Union of sets, Set Intersection, Difference of Sets)
A = {1,2,3,4,5}
B = {4,5,6,7,8}

# union using | operator
# print(A|B) #= {1, 2, 3, 4, 5, 6, 7, 8} 
# union using union() method
# print(A.union(B)) #= {1, 2, 3, 4, 5, 6, 7, 8} 

# intersection using & operator
# print(A&B) #= {4,5}
# intersection using intersection() method
# print(A.intersection(B)) #= {4,5}

# when using difference in sets order follows
#   (A - B) = set of ele only in A but not in B
#   (B - A) = set of ele only in B but not in A
# difference using the - operator
# print("A - B =", A - B) #= A - B = {1, 2, 3}
# print("B - A =", B - A) #= B - A = {8, 6, 7}
#  #
# print("A - B =", A.difference(B)) #= A - B = {1, 2, 3}
# print("B - A =", B.difference(A)) #= B - A = {8, 6, 7}

## Built In Functions:
# len() - it returns the length (the num of elements) in the set
# max() - it returns the largest item in the set
# min() - it returns the smallest item in the set
# sorted() - it returns a new sorted list from elements in the set.
#   it does not sort the set itself
# sum() - it returns the sum of all elements in the set
# 
# Built In Methods:
# add() - it adds an element to the set
# intersection() - returns the set intersection of two sets as a new set
# clear() - removes all the ele from the set
# copy() - returns a copy of the set
# difference() - returns the difference of 2 or more sets as a new set
# discard() - removes an element from the set if it is a member
# isdisjoint() - it returns True if 2 sets have a null intersection
# issubset() - returns True if another set contains this set
# issuperset() - returns true if this set contains another set
# pop() - removes and returnns an abitrary set element
# remove() - removes an element from the set
# union() - returns the union of sets in a new set
# update() - updates the set with the union of itself and others
#  #