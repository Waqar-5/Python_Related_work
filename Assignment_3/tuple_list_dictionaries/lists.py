# A list in Python is a built-in data structure that allows you to store multiple items in a single variable. Lists are ordered, mutable (can be changed), and allow duplicate values.
# A list is created using square brackets [], and elements are separated by commas ,


# Creating a list of numbers
numbers :list = [1, 2, 3, 4, 5]

# Creating a list of different data types
mixed_list : list = [10, "Hello", 3.14, True]

print("list of numbers: ",numbers)

print("mixed_list: ",mixed_list)

print("***********************")

# Accessing Elements in a List
# You can access list elements using indexing (starting from 0).

fruits : list = ["Apple", "Banana", "Cherry", "Mango"]

print("first element: ",fruits[0])  # First element
print("third element: ",fruits[2])  # Third element
print("Last element: ",fruits[-1])  # Last element (negative indexing)


print("****************************")

# Lists are mutable, meaning you can change elements after creation.
print("Modifying a List")

colors :list = ["Red", "Blue", "Green"]
colors[1] = "Yellow" # change Blue to Yellow

print("yellow takes place of blue: ",colors)

print("*****************************")


# . Adding Elements
# append(): Adds an item at the end of the list.
# insert(): Inserts an item at a specific position.
print("List Operations(append, insert):")

animals : list = ["Cats", "Dogs"]
print("Befor operations: ",animals)
animals.append("Elephant") #Adds at the end
animals.insert(1, "Tiger") #Inserts at index 1

print("After operations: ",animals)


print("*****************************")
"""
Removing Elements
remove(): Removes a specific element.
pop(): Removes an element by index (default is last).
del: Deletes an element or the entire list.
"""

print(" Removing Elements....")

number : list = [20, 10, 30, 40, 50]
print(number)
number.remove(30) #removes 30
number.pop(1) # removes element at index 1 (10)
del number[0] #delete first element(20)

print(number)


print("*******************")


print("Slicing a List")
# You can extract part of a list using slicing.

cars :list = ["Toyota", "Honda", "Ford", "BMW", "Audi"]
print("all elements of list: ",cars)

print("From 1 to 3:",cars[1:4]) #From index 1 to 3
print("From start to index 2:",cars[:3]) # From start to index 2

print("From index 2 to the end: ",cars[2:])

print("*************************")

print("Looping Through a List:")
# You can use loops to iterate through a list.

names :list = ["Ali", "Sara", "John"]
for name in names:
    print("for loop :",name)

print("******************************")

numbering : list = [1, 2, 3, 4]
i = 0

while i < len(numbering):
    print("while loop: ",numbering[i])
    i += 1


print("************************")

print("Sorting a List: ")
num1 : list = [5, 6, 3, 9, 1]

num1.sort() # sort in ascending order
print("ascending order: ",num1)

num1.reverse() # reverse the list
print("ascending order: ",num1)


print("*************************")
# Finding Maximum and Minimum
print("Finding Maximum and Minimum: ")

marks : list =  [87, 90, 78, 95, 98]
print("all marks list: ",marks)
print("Max:", max(marks))
print("Min:", min(marks))

print("****************************")
# Copying a List
print("Copying a List: ")

original : list = [1, 2, 3]

print("original list: ", original)

copy_list = original.copy()
print("Copied list: ",copy_list)


print("**************************")
# List Comprehension (Short Way to Create a List)

print("List Comprehension: ")
squares = [x**2 for x in range(1, 6)]
print(squares)


print("*************************")
# Nested Lists
# A list inside another list is called a nested list.
print("Nested Lists: ")

matrix : list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("whole matrix list: ",matrix)
print("frist row: ",matrix[0]) # first row
print("Element at row 2, column 3: ",matrix[1][2]) # Element at row 2, column 3


print("**************************s")

matrix1 : list = [[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]]
print(matrix1)

# Accessing entire second row
print(matrix[1]) # Output: [40, 50, 60]

# Accessing first element of third row
print(matrix1[2][0]) # output: 70

# Accessing last element of first row
print(matrix1[0][2]) # output: 30


print("************************")

print("Sorting by Last Character in Python:")

words : list = ["apple", "banana", "cherry", "date", "fig"]

# sorting by last character
sorted_words = sorted(words, key=lambda word: word[-1])

print(sorted_words)

print(" Reverse Order (Descending): ")
sorted_words_desc = sorted(words, key=lambda word:word[-1], reverse=True)
print(sorted_words_desc)


print("****************************")

common_words = ["apple", "banana", "cherry", "date", "fig"]

# Sorting by length (shortest to longest)
common_sorted_words = sorted(common_words, key=len)
print("Sorting by String Length in Python (key=len): ",common_sorted_words)

common_sorted_words = sorted(common_words, key=len, reverse=True)
print("Sorting in Descending Order (Longest to Shortest): ",common_sorted_words)







