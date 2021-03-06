## Lists:
########################
# lists are ordered collections of multiple values
# lists are mutable, meaning values of lists can e changed 
#       or manipulated over a period of time
# lists allow if to store duplicate values
# list1 = []
# list2 = [1,2,3,4,5,6]
# list3 = ['Jogn', 23, 5.6, True]

# List manipulation:
#   Accessing elements of a list
#   List Slicing
#   updating a list
#   Dleting elements of a list

# names = ["John", "Sam", "Barry", "Lin"]
# print(names)
# print(names[0]) #= john
# print(names[3]) #= lin
# print(names[1:3]) #= sam, lin
# print(names[2:]) #= barry, lin

# marks = [56, 76, 69, 71, 39]
# marks[4] = 43
# print(marks)

# names = ["John", "Sam", "Barry", "Lin"]
# del names[1] #= removed sam
# print(names)

# Concatenation, Repetition, Membership

# lst1 = [1,2,3]
# lst2 = [4,5,6]
# print(lst1+lst2) #= [1, 2, 3, 4, 5, 6] concatentation
# print(lst1*3) #= [1, 2, 3, 1, 2, 3, 1, 2, 3] repetition

# enrolledList = ["sam", 'mike', 'kane', 'nick']
# print("sam" in enrolledList) #= True
# print("samuel" in enrolledList) #= False

# Iterating over lists

# fruits = ['apple', 'mango', 'cherry', 'banana']
# for i in fruits:
#     print(i)

# fruits = ['apple', 'mango', 'cherry', 'banana']
# for i in fruits:
#     if i == 'mango':
#         print("Mango Found")
#         break
# else:
#     print("Mango not found")

# List Functions:
# python has some built in functions for lists: syntax: function(list)
# len(list) -returns the length of the list
# min(list) - returns the elements if the list with the minimum value
# max(list) - returns the elemenets of the list with the maximum value

# nums = [23, 56, 78, 13, 98, 33]
# print(len(nums)) #= 6
# print(max(nums)) #= 98
# print(min(nums)) #= 13

# Python provides a few built in methods to work with lists also:
# method syntax: list.method()
#
# append(element) - adds the passed element to the end of the list
# insert(index, element) - inserts the passed ele at the passed index
# pop() - removes and return the last element from the list
# remove(element) - removes the passed ele from the list
# reverse() - reverse the order of items in a list
# index(element) - return the index of the first matched item
# count(element) - returns the count of how many times the passed element occurs
# 
# names = ['James', 'Sam', 'Nick']
# names.append("Barry")
# #print(names) #= ['James', 'Sam', 'Nick', 'Barry']
# names.insert(1, "Ron")
# #print(names) #= ['James', 'Ron', 'Sam', 'Nick', 'Barry']
# names.remove("Nick")
# print(names) #= ['James', 'Ron', 'Sam', 'Barry']
# 
# Smart Lists:
#   There are instance where we want to create lists at runtime or
#   create a list from another list or to create a list depending on user data
# EX Below is assuming we want to create a list of even nums at runtime

# even = []
# for x in range(1,11):
#     if x%2 == 0:
#         even.append(x)
# print(even) #= [2, 4, 6, 8, 10]
# Here we run a loop in the given range, if num is even then we append it to list
# That being said, theres a bette way... List Comprehension:
#   is an elegant way to define and create a list in python. We can create lists
#   just like mathmatical statements and only in a single line (comprehension has easier syntax)
# Parts to List Comprehension:
#   Output Expression
#   Input Sequence
#   Variable representing the member of the input seq
#   An Optional predicate part

# EX mirroring above smart list ex in list comprehension
# even = [x for x in range(1,11) if x%2 == 0]
# print(even) #= [2, 4, 6, 8, 10]
# x is the output expression
# range(1,11) is the input seq
# x is variable and
# if x%2 == 0 if predicate part/condition `
# You dont always need all the parts though:
# str = "Hello, List"
# charList = [x for x in str]
# print(charList) #= ['H', 'e', 'l', 'l', 'o', ',', ' ', 'L', 'i', 's', 't']
# we broke a string by characters and stored them in a list here

