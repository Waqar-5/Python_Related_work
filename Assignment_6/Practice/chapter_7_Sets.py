# Chapter 07: Sets in Python

"""
This chapter covers:
- What sets are (unordered collections of unique elements)
- Creating sets
- Adding and removing elements
- Set operations (union, intersection, difference)
- Practical exercises to practice sets
"""

print("***********************************\n")

# 1. Creating Sets

# A set of unique numbers
numbers: set[int] = {1, 2, 3, 4, 5}
print("Original set:", numbers)

# Creating an empty set (note: {} creates an empty dict, so use set())
empty_set: set = set()
print("Empty set:", empty_set)

# From a list (duplicates will be removed)
fruits_list = ["apple", "banana", "apple", "orange", "banana"]
unique_fruits: set[str] = set(fruits_list)
print("Unique fruits from list:", unique_fruits)

print("***********************************\n")

# 2. Adding and Removing Elements

# Adding elements
unique_fruits.add("grape")
print("After adding 'grape':", unique_fruits)

# Removing elements
unique_fruits.remove("banana")  # Raises KeyError if not found
print("After removing 'banana':", unique_fruits)

unique_fruits.discard("pineapple")  # Does not raise error if missing
print("After discard 'pineapple' (not in set):", unique_fruits)

print("***********************************\n")

# 3. Set Operations

set_a: set[int] = {1, 2, 3, 4}
set_b: set[int] = {3, 4, 5, 6}

# Union (all unique elements from both sets)
union_set = set_a.union(set_b)
print("Union:", union_set)

# Intersection (common elements)
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Difference (elements in set_a but not in set_b)
difference_set = set_a.difference(set_b)
print("Difference (set_a - set_b):", difference_set)

# Symmetric Difference (elements in either set but not both)
sym_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", sym_diff_set)

print("***********************************\n")

# 4. Checking Membership

print("Is 2 in set_a?", 2 in set_a)
print("Is 5 not in set_a?", 5 not in set_a)

print("***********************************\n")

# 5. Practical Exercises

# EXERCISE 1: Find unique letters in a word entered by the user
word: str = input("Enter a word: ")
unique_letters: set[str] = set(word)
print(f"Unique letters in '{word}':", unique_letters)

print("***********************************\n")

# EXERCISE 2: Compare two lists and print unique elements in each
list1 = input("Enter first list of numbers separated by space: ").split()
list2 = input("Enter second list of numbers separated by space: ").split()

set1 = set(map(int, list1))
set2 = set(map(int, list2))

print("Unique to first list:", set1.difference(set2))
print("Unique to second list:", set2.difference(set1))
print("Common elements:", set1.intersection(set2))

print("***********************************\n")

# Summary
"""
| Operation           | Description                                  | Example                    |
|---------------------|----------------------------------------------|----------------------------|
| set()               | Create a set                                | set([1, 2, 2]) -> {1, 2}  |
| add()               | Add element                                 | s.add(3)                   |
| remove()            | Remove element (error if not found)         | s.remove(2)                |
| discard()           | Remove element (no error if missing)        | s.discard(4)               |
| union()             | All elements from both sets                  | A.union(B)                 |
| intersection()      | Common elements                              | A.intersection(B)          |
| difference()        | Elements in A but not in B                    | A.difference(B)            |
| symmetric_difference() | Elements in A or B but not both            | A.symmetric_difference(B)  |
"""

