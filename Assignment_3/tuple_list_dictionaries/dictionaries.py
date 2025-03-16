# A dictionary is a collection of words or terms, typically arranged alphabetically, with their meanings, pronunciations, usage, and other relevant information.A dictionary is a data structure that stores key-value pairs. It allows fast lookup, insertion, and deletion of elements based on unique keys.


my_dict : dict[str, int, str]= {"name" : "Khan", "age": 25, "city": "Pakistan"}
print(my_dict["name"])

print("***************************")

# Accessing Dictionary Elements
my_dict1 : dict[str, int, str] = {"name":"Ameen", "age": 25, "city": "New York"}
print(my_dict1)

# Accessing a value
print(my_dict1["name"])


# Using get() method (prevents KeyError)
print(my_dict1.get("age")) 


#  Accessing a non-existent key using get() (returns None instead of an error)
print(my_dict1.get("country")) 


print("****************************")
print(" Adding and Updating Dictionary Elements:")
my_dict1["county"] = "USA"
print("Adding other element:", my_dict1)

# Updating an existing value
my_dict1["age"] = 26
print("Updating date 25 to 26",my_dict1)


print("***********************")

print("Removing Dictionary Elements")
# Using pop() - removes and returns the value of a key
age = my_dict1.pop("age")
print("age is removed: ",age)
print("after removing age: ",my_dict1)


# suing del - remove a key
del my_dict1["city"]
print("delete city with key: ",my_dict1)

# Using popitem() - removes the last inserted key-value pair (Python 3.7+)
my_dict1.popitem()
print("remove last element: ",my_dict1)

# # Using clear() - removes all elements
my_dict1.clear()
print("remove all elements by using clear: ",my_dict1)


print("****************************")

# Python provides various built-in methods for dictionaries.
print("Dictionary Methods: ")


sample_dict : dict[str, int, str] = {"name" : "Ameer", "age" : 16, "city" : "Pakistan"}

print("keys: ",sample_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print("Values:",sample_dict.values()) # Output: dict_values(['Alice', 25, 'New York'])
print("Whole dictionary print:",sample_dict.items()) # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

if "name" in sample_dict:
    print("Key exists!") # output: Key exist!

# merging two dictionaries using update()
extr_info = {"country" : "USA", "gender": "Female"}
sample_dict.update(extr_info)
print("updated: ",sample_dict)


print("*********************************")


# Iterating Over a Dictionary
print("Iterating Over a Dictionary")

sample_dict : dict[str, int, str] = {"name" : "Ameer", "age" : 16, "city" : "Pakistan"}
print(sample_dict)
for key in sample_dict:
    print(key, ":", sample_dict[key])

# Iterating over key-value pairs
for key, value in sample_dict.items():
    print(f"{key} -> {value}")


print("*****************************")
#  Nested Dictionary (Dictionary inside a Dictionary)

students : dict[[int, str],[int, str]] = {"Ali": {"age" : 25, "city": "New York"},
"Ahmed": {"age": 30, "city": "Los Angeles"}
}

print("show city from ali key:",students["Ali"]["city"])


print("*********************")

# . Dictionary Comprehension
print("Dictionary Comprehension")
squared_numbers : dict = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension: ",squared_numbers)

print("***************************")
# Dictionary Use Cases
print("Dictionary Use Cases")

text = "hello world"
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)

print("********************************")
#  Converting Two Lists into a Dictionary
print(" Converting Two Lists into a Dictionary:")

keys = ["name", "age", "city"]
values = ["Ali", 20, "New York"]
person_dict = dict(zip(keys, values))
print("zipping keys and values: ",person_dict)

print("*********************************")
# Default Dictionary (Using defaultdict)
print("Default Dictionary (Using defaultdict):")

from collections import defaultdict

default_dict = defaultdict(int)
default_dict["a"] += 1 # Default value is 0
print(default_dict["a"])  # Output: 1
print(default_dict["b"])  # Output: 0 (instead of KeyError)


print("***************************************")
# Ordered Dictionary (Using OrderedDict)
print("Ordered Dictionary (Using OrderedDict):")

from collections import OrderedDict

Ordered_dict = OrderedDict()
Ordered_dict["one"] = 1
Ordered_dict["two"] = 2
Ordered_dict["three"] = 3

print(" # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)]):",Ordered_dict)  # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)])

print("**************************")
# . Dictionary vs. List Performance
print("Dictionary vs. List Performance")

import time

list_item = list(range(1000000))
start = time.time()
999999 in list_item # slow loopup
end = time.time()
print("List loopup time:", end - start)

# Using a dictionary
dict_items = {i: None for i in range(1000000)}
start = time.time()
999999 in dict_items # slow loopup
end = time.time()
print("Dictionary loopup time: ", end - start)