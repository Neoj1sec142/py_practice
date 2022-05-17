# Loops: 
###############################
# 2 types of iteration: 
# Definite: the number of repitition is specified explicitly in advance
# Indefinite: the code block executes until some condition is met
# 
# Different Loops:
# For: used for defitine iteration, that is when the number of iterations is known
# While: used for indefinite iteration, number of iterations is unknown
# 
# Range Function:
# * the range() is abuilt in function in python used when a user need to perform 
#   an action for a specific number of times, used to generate a sequence of numbers 
#   and is commonly used with the for loop
#   * the range function takes mainly 3 arguments start end and step
# start: an integer starting from which the sequence of integers is to be returned
# stop: an integer before which the sequence of integers is to be returned. 
#       The range of integers ends at stop -1
# step(optional):it is an integer value which determines the increment in the sequence

# ex:
# print(list(range(5))) #single argument
#signifies the end of the range (excluded)
# print(list(range(1,5))) # two arguments
# signifies start and end
# print(list(range(1, 10,2))) # three args
#signifies the start, stop, ad steps taken to get there
# print(list(range(70,100,5))) #= [70,75,80,85,90,95]

# For Loops:
# for val in sequence:
#     statements
# Here the value is a variable that takes the value of the itwm inside 
# the sequence on each iteration

# for i in range(5):
#     print(i)
# for i in range(5):
#     print('Python')
# for i in "Python":
#     print(i)

# While Loops:
# execuats a block of code until the condition is met
# while boolean_expression:
#   statement(s)

# i = 0
# while i<3:
#     print("I love Python")
#     i = i+1

# The Break Statement
# if you want to exit the loop before a condition is met 
# you need to do so with a loop control statement(break)
# if the break is present in a nested loop then it terminates
# only thos loops which contain a break statement

str = "Goodmorning"
for i in str:
    if i == "m":
        break 
    else:
        print(i)