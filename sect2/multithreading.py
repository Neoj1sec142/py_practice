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
#   multiple multithreading cores #