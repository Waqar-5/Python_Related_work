# Chapter 04: Strings and Casting in Python

"""
This chapter covers:
- String creation and manipulation
- String methods
- String formatting
- Type casting (converting between strings and other types)
- Practice exercises
"""

# 1. Creating Strings
single_quote_str: str = 'Hello'
double_quote_str: str = "World"
multi_line_str: str = """This is a
multi-line string
example."""

print(single_quote_str)
print(double_quote_str)
print(multi_line_str)

print("*****************************************")

# 2. String Operations

# Concatenation
greeting: str = single_quote_str + " " + double_quote_str
print("Concatenated string:", greeting)

# Repetition
echo: str = "Echo! " * 3
print(echo)

print("*****************************************")

# 3. String Indexing and Slicing
word: str = "Python"

print("First character:", word[0])       # P
print("Last character:", word[-1])       # n
print("Slice (2 to 5):", word[2:5])      # tho
print("Slice (start to 3):", word[:3])   # Pyt
print("Slice (3 to end):", word[3:])     # hon

print("*****************************************")

# 4. Common String Methods
text: str = "  python Programming  "

print("Original text:", repr(text))
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped:", text.strip())
print("Replace 'python' with 'Java':", text.lower().replace("python", "java"))
print("Split into list:", text.split())

print("*****************************************")

# 5. String Formatting

name: str = "Alice"
age: int = 25

# Using f-string (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# Using format()
print("My name is {} and I am {} years old.".format(name, age))

# Using % formatting
print("My name is %s and I am %d years old." % (name, age))

print("*****************************************")

# 6. Type Casting (Converting Types)

num_str: str = "100"
num_int: int = int(num_str)
num_float: float = float(num_int)

print("String to int:", num_int)
print("Int to float:", num_float)

age: int = 30
age_str: str = str(age)
print("Int to string:", age_str)

# Casting input strings to numbers
input_str: str = input("Enter a number: ")
input_num: int = int(input_str)
print("Number plus 10:", input_num + 10)

print("*****************************************")

# 7. Practical Exercises

# EXERCISE 1: Reverse a string
user_str: str = input("Enter a string to reverse: ")
reversed_str: str = user_str[::-1]
print("Reversed string:", reversed_str)

print("*****************************************")

# EXERCISE 2: Check if a string is palindrome
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")  # normalize by removing spaces and lowercase
    return s == s[::-1]

test_str: str = input("Enter a string to check palindrome: ")
if is_palindrome(test_str):
    print(f"'{test_str}' is a palindrome.")
else:
    print(f"'{test_str}' is NOT a palindrome.")

print("*****************************************")

# EXERCISE 3: Format user info
user_name: str = input("Enter your name: ")
user_city: str = input("Enter your city: ")
print(f"{user_name} lives in {user_city}.")

# Summary
"""
| Concept           | Description                            | Example                    |
|-------------------|--------------------------------------|----------------------------|
| String Creation   | Using '', "", or triple quotes for multi-line | 'Hello', "World", '''...''' |
| Indexing/Slicing  | Access parts of string by index       | word[0], word[2:5]          |
| Methods           | Useful functions like lower(), strip(), replace() | text.lower(), text.strip()  |
| Formatting        | f-strings, format(), % operator       | f"{name} is {age} years old"|
| Casting           | Convert between strings and numbers   | int("123"), str(45)         |
"""
