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
# 
# Dictionary Functions:
# Python provides some inprotant functions for dictionaries
# 
# keys() - returns the list of dictionary keys
# values() - returns the list of dictionary values
# clear() - removes all elements of a dictionary creating an empty dictionary
# get(key) - returns the value of the specified key, if no key return none
# items() - returns a list of dictionaries key value pairs in tuple form
# update(dict) - adds specified dictionary(items) key values pairs to the dictionary
# empData = {101:"Bravo", 102:"Asten", 103:"Kerry"}
# print(empData.keys()) #= dict_keys([101, 102, 103])
# print(empData.values()) #= dict_values(['Bravo', 'Asten', 'Kerry'])
# print(empData.items()) #= dict_items([(101, 'Bravo'), (102, 'Asten'), (103, 'Kerry')])
# empData.update({104:"Curan", 105:"Elly"})
# print(empData) #= {101: 'Bravo', 102: 'Asten', 103: 'Kerry', 104: 'Curan', 105: 'Elly'}
# the update method will create a new pair if the key is not found but overwrites exsisting ones
# varDict = {"Asia":["India", "UAE", "China"], 101:"Dalmations"}
# varDict["Asia"].append("Japan") 
# print(varDict) #= {'Asia': ['India', 'UAE', 'China', 'Japan'], 101: 'Dalmations'}
# varDict["Asia"].remove('China')
# print(varDict)

# Iterating Over a Dictionary:
# iterating over a dictionary can be tricky because of its kvp
# this section will show a few different ways of accomplishing this
empData = {101:"Bravo", 102:"Sten"}
# for i in empData:
#     print(i) #= 101 102 only keys
# for i in empData.values():
#     print(i) #= Bravo Sten
# for i in empData.items():
#     print(i) #= (101, 'Bravo') (102, 'Sten')

#  #