# Algorithims:    
- An algorithim is a set of steps or instructions for completing a task. In Computer Science an algorithim is a set of steps a program takes to finish a task. Understanding the algorithim isn't as important as knowing when to apply it. When you have a set of steps you can identify the best way to achieve this 
- Interviewers don't want you to know how to write a specific algorithim they want you to be able to take a problem and break it down into components and evaluate the best route to solving the problem (algorithimic thinking)
- EX: in a given range 1-10 can you guess the number? (num = 7)    
* P1: 1?     
* EX: No Higher    
* P1: 2?    
* EX: No Higher    
* P1: 3?    
* EX: No Higher    
* P1: 4?    
* EX: No Higher    
* P1: 5?    
* EX: No Higher    
* P1: 6?    
* EX: No Higher    
* P1: 7?    
* EX: Yes - 7 tries    

* P2: 5?     
* EX: No Higher    
* P2: 8?    
* EX: No Lower    
* P2: 7?    
* EX: Yes - 3 tries   

- the two different approaches to this may not always show whos option is best until the range grows and the complexity of the search grows the time taken the shortest route will be the most effective route.    
- searching for a value has many different methods
- Knowing that these algorithims are to search for the value they are considered search algroithims
    * P1 Linear Search - simple search - searching sequentially from 1,2,3,4,5,etc... Algorithim definition must contain a specific set of instructions and a clear problem case. 
    - algrorithims should produce a result
    - algrothims need to complete - no inifinites    
- Clearly defined problem statement, input and output
- The steps in the algorithim need to be in a very specific order
- the steps also need to be distict
- the algorithim should produce a result
- should complete in a finite amount of time
- must result in same output everytime.


* Break down the problem into as many smaller problems as possible that are clearly defined
* Time Complexity - is a mesure of how long it will take the algorithim to run
* Space Complexity - amount of memory taken on the computer while running the algorithim 
* When using binary search algo the items need to be sorted before the search can begin
* When evaluating we time complexity we always want to see the worst case efficiency

- **Big O** is the theoretical definition of the complexity of an algorithm as a function of the size

* Notation use to descibe complexity
* O is a uppercase letter

Linear Search O(n)
Binary search O(log n) - wayyyyy faster

constant time O(1)
Linear Time O(n)
Logarithmic Time O(log n) 
quadratic Time O(n^2)
cubic runtime O(n^3)
quasilinear runtime O(n log n) - merge sort worst case
polynomial runtime O(n^k) where k = a given number -efficent and often 
        used
exponential runtime O(x^n) = brute force not efficient 
- each char in a password can be 1 in 69 characters via 8 char pass 
    8^69 possible options
- which is why the longer your password the safer
* Facotrial/Combinitorial - n! = n(n-1)(n-2)until you reach 1
    * EX: 3!: 3 x 2 x 1 = 6
    * EX2: 4!: 4 x 3 x 2 x 1 = 24

### How to determine the worst case complexity of an alorithm:
* binary search - best case O(1) - worst case O(log n)
Selection Sort O(n^2)
quick sort O(n^2) - best used with random pivot rather than first 
    pivot
Merge sort O(n log n)
