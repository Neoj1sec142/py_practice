## DICTIONARIES ###
###############################
# is an unordered and mutable collections of items
# Each item of a dictionary has a key/value pair
# one can retrieve values when the key is known
# each key in the dictionary is unique values can be repeated
# dict1 = {}
# dict2 = {1:"John", 2:"Sam"}
# studentsEnrolled ={
# "John":"Python",
# "Sam":"Java",
# "Nick":["Java", "JavaScript"]
# }
# print(studentsEnrolled)

# Manipulating Dictionaries:
#   Dictionarys in python are unordered so we cannot use the concept of
#   an index to access and manipulate elements of a dictionary
#   instead we use the concept of keys since those are unique
#   so the values can be uniquely identified with the keys
# 
#  Keys can be used either insdie [] or with the get() method
#  [] returns a key error if key not found
#  get() returns none if key not found
# example = {1:"John", 2:"Nick"}
# example[1]= "Den"
# example[3]= "Sim"
# print(example) #= {1: 'Den', 2: 'Nick', 3: 'Sim'}
# if the key value pair is present then it gets updated if not it gets created
# del example[1] #= we can delete KVP by key or the whole dictionary with del
#  #