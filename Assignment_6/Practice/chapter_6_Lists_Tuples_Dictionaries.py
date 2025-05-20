# Chapter 06: Lists, Tuples, and Dictionaries in Python

"""
This chapter explains:
- Lists: ordered, mutable collections
- Tuples: ordered, immutable collections
- Dictionaries: key-value pairs (unordered)
- Common operations and methods for each
- Practical exercises to try out
"""

print("***********************************\n")

# 1. Lists

# Creating a list of fruits
fruits: list[str] = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Adding an item
fruits.append("orange")
print("After append:", fruits)

# Inserting at a specific position
fruits.insert(1, "blueberry")
print("After insert at index 1:", fruits)

# Removing an item
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Accessing elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing a list
print("First two fruits:", fruits[:2])

# Looping through a list
print("Looping through fruits:")
for fruit in fruits:
    print(f"- {fruit}")

print("***********************************\n")

# 2. Tuples

# Tuples are like lists but immutable (cannot change after creation)
coordinates: tuple[int, int] = (10, 20)
print("Coordinates tuple:", coordinates)

# Accessing tuple elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Trying to change a tuple element would cause an error:
# coordinates[0] = 15  # This will raise TypeError

# You can unpack tuples easily
x, y = coordinates
print(f"Unpacked coordinates: x = {x}, y = {y}")

print("***********************************\n")

# 3. Dictionaries

# Dictionaries store data in key-value pairs
person: dict[str, str | int] = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print("Person dictionary:", person)

# Accessing values by key
print("Name:", person["name"])
print("Age:", person.get("age"))  # get() is safer, won't error if key missing

# Adding a new key-value pair
person["job"] = "Engineer"
print("After adding job:", person)

# Changing a value
person["age"] = 31
print("After updating age:", person)

# Removing a key-value pair
removed = person.pop("city")
print("Removed city:", removed)
print("After removal:", person)

# Looping through dictionary keys and values
print("Person info:")
for key, value in person.items():
    print(f"{key}: {value}")

print("***********************************\n")

# 4. Practical Exercises

# EXERCISE 1: Create a list of your favorite movies and print them numbered
movies: list[str] = []
n = int(input("How many favorite movies do you want to enter? "))
for i in range(n):
    movie = input(f"Enter movie #{i + 1}: ")
    movies.append(movie)

print("\nYour favorite movies:")
for idx, movie in enumerate(movies, 1):
    print(f"{idx}. {movie}")

print("***********************************\n")

# EXERCISE 2: Create a tuple representing your birthdate (year, month, day)
birthdate: tuple[int, int, int] = (
    int(input("Enter birth year: ")),
    int(input("Enter birth month: ")),
    int(input("Enter birth day: "))
)
print(f"Your birthdate tuple is: {birthdate}")

print("***********************************\n")

# EXERCISE 3: Create a dictionary to store a book's details and display them
book: dict[str, str | int] = {
    "title": input("Enter book title: "),
    "author": input("Enter author name: "),
    "year": int(input("Enter publication year: "))
}

print("\nBook Details:")
for key, value in book.items():
    print(f"{key.capitalize()}: {value}")

print("***********************************\n")

# Summary
"""
| Data Structure | Mutable | Syntax Example                      | Notes                          |
|----------------|---------|-----------------------------------|--------------------------------|
| List           | Yes     | [1, 2, 3]                        | Ordered, changeable, allows duplicates |
| Tuple          | No      | (10, 20)                        | Ordered, immutable              |
| Dictionary     | Yes     | {'key': 'value'}                 | Key-value pairs, unordered     |
"""
