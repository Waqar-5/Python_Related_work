# Chapter 09: Exception Handling in Python

"""
This chapter covers:
- What exceptions are and why we need to handle them
- Try, except blocks for catching errors
- Using else and finally clauses
- Raising exceptions manually
- Common exception types
- Practical exercises to handle errors gracefully
"""

print("***********************************\n")

# 1. What is an Exception?

# Exceptions are errors that occur during program execution,
# which can cause the program to stop if not handled.

# Example: Dividing by zero raises an exception
# Uncomment below to see the error
# print(10 / 0)  # ZeroDivisionError

print("***********************************\n")

# 2. Handling Exceptions with try and except

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print("An unexpected error occurred:", e)

print("***********************************\n")

# 3. Using else and finally

try:
    value = int(input("Enter a positive integer: "))
    if value < 0:
        raise ValueError("Negative value entered!")
except ValueError as ve:
    print("ValueError:", ve)
else:
    print("You entered:", value)
finally:
    print("This block runs no matter what (cleanup code).")

print("***********************************\n")

# 4. Raising Exceptions Manually

def check_age(age: int) -> None:
    if age < 18:
        raise Exception("Age must be 18 or older!")
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except Exception as ex:
    print("Exception caught:", ex)

print("***********************************\n")

# 5. Common Exception Types

# IndexError example
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("IndexError: List index out of range.")

# KeyError example
try:
    d = {"name": "Alice"}
    print(d["age"])
except KeyError:
    print("KeyError: Key not found in dictionary.")

print("***********************************\n")

# 6. Practical Exercises

# EXERCISE 1: Handle multiple exceptions when converting input to int
try:
    val = int(input("Enter an integer: "))
    print("You entered:", val)
except ValueError:
    print("Oops! That's not a valid integer.")

print("***********************************\n")

# EXERCISE 2: Write a function that divides two numbers with exception handling
def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
division_result = safe_divide(num1, num2)
if division_result is not None:
    print("Division result:", division_result)

print("***********************************\n")

# Summary
"""
| Keyword   | Description                                |
|-----------|--------------------------------------------|
| try       | Block of code to attempt execution        |
| except    | Block to handle exceptions                 |
| else      | Runs if no exception occurred              |
| finally   | Runs always (for cleanup)                   |
| raise     | Manually throw an exception                 |
"""
