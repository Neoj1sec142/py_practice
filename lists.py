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
