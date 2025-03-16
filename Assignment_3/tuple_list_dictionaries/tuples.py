"""
A tuple is an immutable (unchangeable) and ordered collection of items in Python. It allows storing multiple items in a single variable. Tuples are similar to lists but cannot be modified after creation, making them faster and more memory-efficient.

Creating Tuples
Tuples are defined using parentheses ( ), with elements separated by commas.
"""


empty_tuple : tuple = () # Empty tuple
single_element_tuple : tuple[int] = (42,) # A single-element tuple (comma is required)
fruits: tuple[str,...] = ("apple", "banana", "cherry") # Tuple with multiple elements

print("empty tuple: ", empty_tuple)
print("sinlge element conating tuple:", single_element_tuple)
print("tuples elements: ",fruits) # Output: ('apple', 'banana', 'cherry')

print("******************************")

"""
Tuple Indexing and Slicing
Tuples support indexing (to access individual elements) and slicing (to get a sub-part of the tuple).

"""

numbers : tuple[int,...] = (10, 20, 30, 40, 50)

print(numbers)
print("first element: ",numbers[0]) # Output: 10  (First element)
print("second element: ",numbers[-1]) #Output: 50  (Last element)

print("prints from 1 to 4(3 elements): ",numbers[1:4])  # Output: (20, 30, 40)

print("***********************")

# print("Immutable Nature of Tuples")

animals : tuple[str,...] = ("cat", "dog", "rabbit")
# Uncommenting the next line will cause an error
# animals[1] = "elephant"  # TypeError: 'tuple' object does not support item assignment


print("**********************")
print("Tuple Operations: ")

tuple1 : tuple[int,...] = (1, 2, 3)
tuple2 : tuple[int,...] = (4, 5, 6)
print("tuple1 elements: ",tuple1)
print( "tuple2 elements: ", tuple2)
combined = tuple1 + tuple2
print("Addition tuple1 and tuple2: ",combined)

# repetition
repeated = ("Hello",) * 3
print("Repetition: ", repeated)

# tuple length
print("combined tuple length:", len(combined))

print("************************")
# Tuple Unpacking
# Tuple unpacking allows assigning values directly to variables.

print("Tuple Unpacking")
person : tuple[str, int, str] = ("Khan", 25, "Doctor")
print(person)
name, age, profession = person

print("Name: ",name)
print("age:" ,age)
print("profession: ",profession)

print("************************")
# Tuple Methods
# Tuples have only two built-in methods: .count() and .index().

nums : tuple[int] = (1, 2, 3, 2, 2, 4, 5) 
print(nums.count(2)) # Output: 3 (Number of times 2 appears)

print(nums.index(4))  # Output: 5 (Index of first occurrence of 4)


print("***********************")
# Understanding id() in Tuples
print("Understanding id() in Tuples")


tuple_1 : tuple[int,...] = (1, 2, 3)
tuple_2 : tuple[int,...] = (1, 2, 3)
print("tuple_1: ", tuple_1)
print("tuple_2: ", tuple_2)
# Printing memory addresses

print("id(tuple_1) =", id(tuple_1))
print("id(tuple_2) =", id(tuple_2))

# Checking if both tuples are equal
print("tuple_1 == tuple_2:", tuple_1 == tuple_2)

# Checking if both tuples have the same memory location
print("tuple_1 is tuple_2:", tuple_1 is tuple_2)


