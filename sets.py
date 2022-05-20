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

#  #