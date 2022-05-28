## MULTI-THREADING: ##
# While humans multitask computers multithread
# multithreading is the process by which computers erpform various
#   tasks simultaneously
# 
# Multiple Tasks: (Building the Foundation)
# Each task on the computer is handled by a process. 
#   Each process is handled by something called a thread
# Thus, at the most basic level, a thread is responsible for 
#   executing the various tasks on the computer
# Task -> Process -> Thread
# Process: is basically the program in exectuion. 
#   When you start an application on your computer, 
#   the operating system creates a process
# in simple words a process is an instance of a computer 
#   program the is being executed
# Thread: is an entity within a process that can be scheduled for execution. 
#   Also it is the smallest unit of processing that can be performed 
#   in and Operating System 
# In simple words a thread is a sequence of instructions within 
#   a program that can be executed independantly of other code
# 
# Multithreading is defined as the ability of processor to execute 
#   multiple threads concurrently 
# The central processing unit (CPU) or a single core in a 
#   multi-core processor executes multiple processes or 
#   threads concurrently, appropraitly supported by the operating system
# Multiple threads may execute individually while sharing their process resources.
#   The purpose of multithreading is to run multiple tasks and function 
#   calls at the same time
# Multithreading difers from multiprocessing, as with 
#   multithreading the processes and threads have to share 
#   the resources of a single or multiple-cores
# While multiprocessing systems include multiple processing units
# Multithreading aims to increase the untilization of a single core
#    by using thread-level as well as instruction-level parallesim
# As the two techniques are complimentary, they are sometimes combined 
#   in  systems with multiple multithreading CPUs and in CPUs with 
#   multiple multithreading cores
# 
# consider thee follwing code::
#  #
# class Example:
#     def run(self):
#         for i in range(5):
#             print("Hello from Example")

# class ExampleTwo:
#     def run(self):
#         for i in range(5):
#             print("Hello from ExampleTwo")

# example = Example()
# exampleTwo = ExampleTwo()
# example.run()
# exampleTwo.run()
# This is a bad ex because they cannot be use at the same time #
# Modern technologies should be able to deal with such situations
#   and allow the user to use various functionalities simultaneously
# 
# Python provides the following two modules to implement threading in Python
# thread module (depreciated since Py3)
# threading module - is the high-level implementation of threading in python and 
#           the de facto standard for managing multithreading applications
#           -this module defines manu classes, funcitons, and more
# 
# Info About Threading Module:
#   Factory Functions:
#       active_count() - returns the count of Tread objects which are still alive
#       current_thread() - returns ther current object of Thread class
#       enumerate() - returns a list of all active Tread objects
#       isDaemon() - returns true is the thread is a daemon
#       isAlive() - returns true if thread is alive #
#       Lock() 
#       RLock()
#       Semaphore()
#   Objects:
#       Lock Object: acquire(), release()
#       RLock Object: acquire(), release(), blocking
#   Classes:
#       Thread - the thread class is the primary class that defines the 
#               template and operations of a thread in python, it provides all the 
#               major functionalites required to create and manage a thread
#               - the most simple way to create a multithreaded python app is to declare
#                   a class that inherits from the Thread class and overrrides its run() method
#               - every Thread class has a run() method, and to implement threading, one 
#                  should override the run() method in their respective classes
#               - once we inherit a class from the Thread class in the threading module, we can
#                   create a Thread object from it
#               -Normallu the whole program is executed by something called the main() thread, but 
#                   when we create a thread object, each object represents an activity to be performed
#                   in a separate thread of control
#           Methods of the Thread class:
#               run() - denotes the activity of a thread and can be overridden by a class that extends the Thread class
#               start() - starts the activity of a thread. It must be called only once for each thread because it will throw
#                       a runtime error if called multiple times
#               join() - blocks the execution of other code until the thread on which the join() method was called heys terminated
#           - once a thread object has been made, the start() method can be invoked to begin the execution of the activity
#               and the join() method can be used to block all other code till the current acitivty finishes #
#       Timer
#       Condition
#       Event
#       local
#       Semaphore
#   Exceptions:
#       Thread Error - raised for various thread related errors, some systems may
#               throw a runtime error in place of a thread error
#  #
# from threading import *
# class Example(Thread):
#     def run(self):
#         for i in range(400):
#             print("Hello from Example")

# class ExampleTwo(Thread):
#     def run(self):
#         for i in range(400):
#             print("Hello from ExampleTwo")

# example = Example()
# exampleTwo = ExampleTwo()
# example.start()
# exampleTwo.start()
# Obviously the above doesnt get the requested 1 after the other
#   to tdo this we need the time module to ask our loop for a second 
#   before executing the next one this process needs to be repeated
#   execute -> wait -> execute
# We can use the sleep() method which accepts time in seconds as parameters and 
#   makes the code go to sleep(wait) for that amount of time #
# from threading import *
# from time import sleep

# class Example(Thread):
#     def run(self):
#         for i in range(400):
#             print("Hello from Example")
#             sleep(1)

# class ExampleTwo(Thread):
#     def run(self):
#         for i in range(400):
#             print("Hello from ExampleTwo")
#             sleep(1)

# example = Example()
# exampleTwo = ExampleTwo()
# example.start()
# sleep(0.1)
# exampleTwo.start()

# Each process us handled by a thread, 
#   therefore, when we execute and Python prgoram, there is one thread
#   already running by default called the main thread
# The main thread is responsible for the execution of the programs in Python
# The problem with this is that when its executed the two thrreads its job is done its over
#   and it didnt tell the program that the other were still running when it printed the ast statemtn 
# We need to handle this
#   We would handle this with the join() method as it blocks code from executing until its done
# The join() method blocks the execution of other code (work of main thread) until
#    the thread later on which the join() method is called gets teminated #

# from threading import *
# from time import sleep

# class Example(Thread):
#     def run(self):
#         for i in range(20):
#             print("Hello from Example")
#             sleep(1)

# class ExampleTwo(Thread):
#     def run(self):
#         for i in range(20):
#             print("Hello from ExampleTwo")
#             sleep(1)

# example = Example()
# exampleTwo = ExampleTwo()
# example.start()
# sleep(0.1)
# exampleTwo.start()
# example.join()
# exampleTwo.join()
# print("End of program")


# Implementing multithreading is often referred to as concurrent programming
# Creating apps tha support concurrency is the need of the hour, but 
#   working with concurrent programming is a bit complicated
# When we talk about multithreading and concurrent programming, one must
#   keep in mind the foolowing two situations that you might encounter:
#           Deadlocks
#           Race conditions
# Deadlock - a situation where a set of processes are blocked because each
#           process is holding a resource and waitinf for another resource 
#           acuired by some other process
#           - The best way to understand deadlocks is by using the classic 
#               computer science example problem known as the Dining 
#               Philosophers Problem:
# Dining Philosophers Problem - Five philosophers are seated on a round table with 
#           five plates of spaghetti and five forks
#           - At any given time a philosopher must either eat or think
#           - Moreover, a philosopher must take the two forks adjacent to him
#               (i.e., the left and right forks) before he can eat the spaghetti
#               The problem of deadlock occurs when all five philosophers pick up their 
#               right forks simultaneously
#           - Since each of the philosophers has one fork, they will all wait for the 
#               others to put their fork down. As a result, none of them will be able to 
#               eat spaghetti
#           -Similarly in a concurrent system a deadlock occurs when different threads 
#               or processes (philosophers) try to acquire the shared system resource
#               (forks) at the same time
#           - As a result non e of the processes get a chance to execute because they are 
#               all waiting for another resource held by some other process 
# Race Conditions - is an undesirable situation that occurs when a decive or system
#           attemps too perform two or more operations at the same time, but, 
#           because of the nature of the device or system, the operations must
#           be done in the proper sequence to be done correctly
#           - In a real multithreading environment, the threads can overlap, and the value 
#               which was retireved and modified by a thread can change in between 
#               when some other thread accesses the same value
# 
# Synchronization:
# Deadlocks and race conditions are the 2 main problems that can occur in
#   a multithreaded pythoon app
# To deal with race condititions, deadlocks and other thread-based issues,
#   the threading module provides the Lock object
# In the threading module, for efficient multithreading, a primitive lock is used
#   This lock helps up in the synchronization of two or more threads
# The simple idea is that when a thread wants access to a specific resource, 
#   it acquries a lock for that resource
# Once a thread locks a particular resource, no other 
#   thread can access it until the lock is released
# As a result, the changes to the resource will be atomic i.e. no half-modifidied 
#   values being avaliable to other threads, and race conditions will be averted
# 
# Lock Object:
# - A lock is a low-level sychronization primitive impleented by the the threading module
#       At any given time, a lock can be in one of two states: locked or unlocked
# Main methods of Lock Object:
#   acquire() - when the lock-state is unlocked, calling the acquire() metho will change
#           the state to locked and return. However if the state is locked, the call
#           acquire() is blocked until the release() method is called by some other thread
#   release() - is used to set the stateto unlocked, that is to release a lock. It can
#           be called by any thread, not necessarily the one that acquired the lock #

# There are situations when we want part of our code to acquire all of the resources and
#       execute their job first, lets do that with a lock obj #

# from threading import *
# import threading
# from time import sleep

# lock = threading.Lock()

# class Example(Thread):
#     def run(self):
#         for i in range(20):
#             lock.acquire()
#             print("Lock Acquired")
#             print("Hello from Example")
#             sleep(1)
#             lock.release()
# class ExampleTwo(Thread):
#     def run(self):
#         for i in range(20):
#             lock.acquire()
#             print("Lock 2 Acquired")
#             print("Hello from ExampleTwo")
#             sleep(1)
#             lock.release()
# example = Example()
# exampleTwo = ExampleTwo()
# example.start()
# sleep(0.1)
# exampleTwo.start()
# example.join()
# exampleTwo.join()
# print("End of program")