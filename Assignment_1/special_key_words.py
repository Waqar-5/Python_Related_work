# Special Keywords in python

""""
Python has reserved keywords that have special meaning and cannot be used as variable names.

"""

# below is the list of special keywords
"""

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


"""
import keyword # type: ignore
print(keyword.kwlist)

print("******************************")	
# Import keywords
#1. Booleans keywords (True, False, None)

x = True
y = False
z = None
print(x, y, z)

# 2. Conditional Statements (if, elif, else)
num = 12
if  num> 0:
    print("Postive Number")
elif num == 0:
    print("Zero")
else: 
    print("Negative Number")


print("*****************************")

# 3. Looping Keywords (for, while, break, contineue, pass)

for i in range(6):
    if i == 4:
        break # stops the loop when i = 4
    print(i)


print("*****************************")

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue # skips the loop when x = 3
    print(x)


print("*****************************")

# 4. Function Keywords (def, return)

def add(x, y):
    return x + y

print(add(2, 3))

print("*****************************")

def greet(name):
    return f"Hello, {name}"

print(greet("Waqar"))

print("*****************************")

# Exception Keywords (try, except, finally, raise)

try:
    x = int(input("Enter a number: "))
    print(x)
except ValueError:
    print("Invalid input. Please enter a valid number.")

print("*****************************")

try: 
    x = 1/ 0 # causes an error
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")

print("*****************************")


# 6. Class and Object Keywords (class, object)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self): 
        print("Stopping the car")

my_car = Car("Toyota", "Camry", 2022)  
my_car.start()
my_car.stop()

print("*****************************")

class Car: 
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"This is a {self.brand} Car.")


my_car = Car("Tesla")
my_car.display()


print("****************************")


# 7. Importing Module(import, from, as)

import math
from math import sqrt as squar_root

print(math.pi)
print(squar_root(16))


print("*****************************")

# 8. Lambda function (lambda)
square = lambda x: x * x
print(square(5))


print("***************************")

# 9. Global and Nonlocal(global, nonlocal)

x = 10

def modify():
    global x
    x = 20

modify()
print(x)
