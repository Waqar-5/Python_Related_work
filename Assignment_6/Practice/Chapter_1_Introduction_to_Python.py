# Chapter 01: Introduction to Python

"""
This chapter introduces the foundational concepts of Python programming, including:
- Basic syntax
- Variables
- Comments
- Input/Output operations
"""

# 1. Printing Output
print("Hello, World!")

# 2. Variables
name = "Alice"
age = 25
is_student = True

# 3. Comments
# This is a single-line comment

"""
This is a
multi-line comment
"""

# 4. Input from User
name = input("Enter your name: ")
print("Hello,", name)

# 5. Basic Data Types
x = 10          # Integer
y = 3.14        # Float
name = "Bob"    # String
is_active = False  # Boolean

# 6. Type Checking
print(type(name))  # Output: <class 'str'>

# Practice Exercise
# Take two numbers from user and print their sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum is:", sum)

# Summary (for reference)
"""
| Concept        | Description                                |
|----------------|--------------------------------------------|
| print()        | Outputs data to the screen                 |
| input()        | Accepts user input                         |
| Variables      | Used to store values                       |
| Comments       | Explain your code                          |
| Data Types     | int, float, str, bool                      |
| type()         | Checks the type of variable                |
"""
