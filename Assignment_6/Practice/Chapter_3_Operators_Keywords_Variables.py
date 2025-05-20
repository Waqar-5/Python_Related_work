# Chapter 03: Operators, Keywords, and Variables

"""
This chapter covers:
- Variables with type annotations
- Python keywords and naming rules
- Arithmetic, comparison, logical, and assignment operators
- Practice exercises
"""

# 1. Variables with Type Annotations
apples: int = 10
price_per_apple: float = 0.5
is_available: bool = True
fruit_name: str = "Apple"

print(f"I have {apples} {fruit_name}s, each costs ${price_per_apple}")

# 2. Keywords in Python
# Keywords are reserved and cannot be used as variable names.
# Examples: if, else, for, while, def, class, return, True, False, None, and, or, not

is_valid: bool = True
if is_valid:
    print("This is valid!")

# 3. Operators

# a) Arithmetic Operators
a: int = 10
b: int = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)      # float division
print("a // b =", a // b)    # floor division
print("a % b =", a % b)      # modulus
print("a ** b =", a ** b)    # exponentiation

# b) Comparison Operators
x: int = 5
y: int = 3

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# c) Logical Operators
val1: bool = True
val2: bool = False

print("val1 and val2:", val1 and val2)
print("val1 or val2:", val1 or val2)
print("not val1:", not val1)

# d) Assignment Operators
x = 10
print("Initial x:", x)
x += 5  # equivalent to x = x + 5
print("After x += 5:", x)
x *= 2  # equivalent to x = x * 2
print("After x *= 2:", x)

# 4. Variable Naming Rules and Best Practices
user_age: int = 25
total_price: float = 99.99
first_name: str = "John"

print(f"User: {first_name}, Age: {user_age}, Total Price: ${total_price}")

# 5. Practice Exercises

# Exercise 1: Calculate the area of a rectangle
length: float = float(input("Enter length of rectangle: "))
width: float = float(input("Enter width of rectangle: "))
area: float = length * width
print("Area of rectangle:", area)

# Exercise 2: Swap two variables without a temporary variable
a: int = 5
b: int = 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# Exercise 3: Check if a number is positive, negative, or zero
num: int = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")




"""
Summary:
- Variables store data and can have explicit type annotations
- Keywords are reserved and cannot be used as identifiers
- Operators include arithmetic, comparison, logical, and assignment
- Proper naming conventions improve code readability
"""


# Chapter 03: Operators, Keywords, and Variables (Extended with Identity and Membership Operators)

"""
This chapter covers:
- Variables with type annotations
- Python keywords and naming rules
- Arithmetic, comparison, logical, assignment operators
- Identity operators (is, is not)
- Membership operators (in, not in)
- Practice exercises
"""

# ... [Previous content remains unchanged above]

print("*****************************************")

# 6. Identity Operators
# Identity operators compare the memory locations of two objects.

a: int = 10
b: int = 10
c: list = [1, 2, 3]
d: list = c  # d references the same list object as c
e: list = [1, 2, 3]  # a new list object with the same values

print("a is b:", a is b)         # True because small integers are cached and share memory
print("c is d:", c is d)         # True, both refer to the same object
print("c is e:", c is e)         # False, different objects even if values are the same

print("a is not b:", a is not b) # False
print("c is not e:", c is not e) # True

print("*****************************************")

# 7. Membership Operators
# Membership operators test whether a value is found in a sequence (like list, string, tuple)

numbers: list[int] = [1, 2, 3, 4, 5]

print("3 in numbers:", 3 in numbers)       # True, 3 is in the list
print("7 in numbers:", 7 in numbers)       # False, 7 is not in the list
print("7 not in numbers:", 7 not in numbers)  # True

word: str = "Python"

print("'y' in word:", 'y' in word)          # True
print("'z' not in word:", 'z' not in word)  # True

print("*****************************************")

# Summary of added operators
"""
Identity Operators:
- is      : Returns True if both variables point to the same object
- is not  : Returns True if variables point to different objects

Membership Operators:
- in      : Returns True if a value exists in the sequence
- not in  : Returns True if a value does not exist in the sequence
"""

