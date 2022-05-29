## CodeWars Python:

# This is my answer capitalize all words in a string with contractions
# def to_jaden_case(string):
#     res = ' '.join(elem.capitalize() for elem in string.split())
#     return res

# my answer to your a square (7 kyu)
#Checks to see if any given integer is a perfect square
# import math
# def is_square(n):
#     if n>=0 and math.sqrt(n) == math.floor(math.sqrt(n)):
#         return True
#     else:
#         return False

# my answer to Build a pile of Cubes (6 kyu)
#Your task is to construct a building which will be a pile of n cubes. 
#   The cube at the bottom will have a volume of n^3, the cube above will 
#   have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

#You are given the total volume m of the building. Being given m can you 
#   find the number n of cubes you will have to build?

#The parameter of the function findNb (find_nb, find-nb, findNb, ...) 
#   will be an integer m and you have to return the integer n such as 
#   n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

# def find_nb(m):
#     op = 1
#     ck = 0
#     while ck <= m:
#         ck += op **3
#         if ck == m: return op
#         op += 1
#     return -1
            