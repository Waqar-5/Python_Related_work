# Built-in Module
import math 

print("Suare of 5 is :",math.sqrt(25)) #output 5.0
print("factorial of 5 is :",math.factorial(5))   # 5! → 120
print("value of pi is : ",math.pi)             # Value of Pi → 3.14159...


print("**********************************")

#  random — For Generating Random Numbers
import random
print("Random number between 1 and 10 is :",random.randint(1,10)) #output 6
print("select a element from random choice : ",random.choice(["apple", "banana", "cherry"])) #output banana
# print(random.choice([1, 2, 3, 4, 5])) #output 5

print("*****************************")

#  datetime — For Working with Dates and Time
import datetime
now = datetime.datetime.now()
print("Current date and time is :",now) #output 2023-10-05 14:48:17.123456
print("Current year is :",now.year) #output 2023
print("Current month is :",now.month) #output 10
print("Current day is :",now.strftime("%A")) #output Thursday



print("**********************************")

# os — For Interacting with the Operating System

import os 
print("Current working directory is :",os.getcwd()) #output /home/user
print("List of files in current directory is :",os.name) #output posix


print("*************************")

# statistics — For Statistical Calculations
import statistics
data = [10, 20, 30, 40, 50]
print("Mean of data is :",statistics.mean(data)) #output 30
print("Median of data is :",statistics.median(data)) #output 30.0

print("********************************")

#  time — For Time-related Functions
import time

print("Start")
time.sleep(2)                  # Pause for 2 seconds
print("End after 2 seconds")
