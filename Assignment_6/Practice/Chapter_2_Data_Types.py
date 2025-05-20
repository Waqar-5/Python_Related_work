# Chapter 02: Data Types in Python

"""
This chapter explains the different data types in Python:
- Numbers (int, float, complex)
- Strings
- Booleans
- Type Conversion (Explicit & Implicit)
- Practical Exercises
"""

# 1. Numeric Types

# Integer
apples:int = 10
print("I have", apples, "apples.")   # Output: I have 10 apples.

# Float(decimal number)
price:float = 2.5
print("The price of an apple is $", price)  # Output: The price is 19.99  # Output: The price of an apple is $ 2.5

# Complex number(used in scientific computing)
complex_number:complex = 3 + 4j
print("Complex number:", complex_number)  # Output: Complex number: (3+4j)

print("*****************************************")


# Implicit Type Conversion
# Python automatically converts int to float when needed
result: float = apples + price
print("Result of int + float:", result)  # Output: 29.99
print("Type of result:", type(result))  # Output: <class 'float'>


print("*****************************************")

# 2. String Type
message: str = "Hello, World!"
print(message)  # Output: Hello, World!



# Multi-line string
paragraph: str = """This is a multi-line
string that spans across
several lines."""
print(paragraph)

print("*****************************************")

# String Indexing and Slicing
name: str = "Python"
print("First letter:", name[0])      # Output: P
print("Last letter:", name[-1])       # Output: n
print("First three letters:", name[:3])  # Output: Pyt


print("*****************************************")

# 3. Boolean Type
is_valid: bool = True
print("Is valid:", is_valid)  # Output: Is valid: True
is_valid = False
print("Is valid:", is_valid)  # Output: Is valid: False

# Boolean from expression
is_greater: bool = 10 > 5
print("Is 10 greater than 5?", is_greater)  # Output: True


print("*****************************************")

# 4. Type Conversion
# Explicit Type Conversion
num_str: str = "100"
num_int: int = int(num_str)
print("String to int:", num_int)  # Output: 100

num_float: float = float(num_int)
print("Int to float:", num_float)  # Output: 100.0



age: int = 20
age_str: str = str(age)
print("Age as string:", age_str)  # Output: '20'

# Boolean conversion
print("bool(0):", bool(0))           # Output: False
print("bool(1):", bool(1))           # Output: True
print("bool(''):", bool(''))         # Output: False
print("bool('hello'):", bool('hello'))  # Output: True

print("*****************************************")

# 5. Checking Data Types with type()
print(type(apples))      # <class 'int'>
print(type(price))       # <class 'float'>
print(type(message))     # <class 'str'>
is_sunny: bool = True
print(type(is_sunny))    # <class 'bool'>


print("*****************************************")


# 6. Practical Exercises

# EXERCISE 1: Convert temperature from Celsius to Fahrenheit
celsius: float = float(input("Enter temperature in Celsius: "))
fahrenheit: float = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

print("*****************************************")

# EXERCISE 2: Check if a number is even or odd
num: int = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("*****************************************")

# EXERCISE 3: Create a short user profile
user_name: str = input("Enter your name: ")
user_age: int = int(input("Enter your age: "))
height: float = float(input("Enter your height in meters: "))
is_student: bool = input("Are you a student? (yes/no): ").lower() == 'yes'




print("\n--- User Profile ---")
print("Name:", user_name)
print("Age:", user_age)
print("Height:", height, "meters")
print("Student:", is_student)

# Summary
"""
| Type      | Description                      | Example             |
|-----------|----------------------------------|---------------------|
| int       | Integer numbers                  | 5, -10              |
| float     | Decimal numbers                  | 3.14, -0.5          |
| complex   | Complex numbers                  | 2 + 3j              |
| str       | Text/String                      | "hello"             |
| bool      | Boolean (True/False)             | True, False         |

Implicit Conversion: Automatically handled by Python when combining compatible types.
Explicit Conversion: Manually converting one type to another using functions like int(), float(), str(), etc.
"""

