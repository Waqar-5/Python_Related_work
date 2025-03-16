""" All about Sets

In Python, a set is an unordered collection of unique elements. Sets are useful for removing duplicates, performing mathematical set operations, and handling unordered data efficiently.
create a set using curly braces {} or the set() function.
"""

# examples 

my_set : set = {1,2,3,4,5,6}
print(my_set)

# empty set

empty_set = set()  # Note: {} creates an empty dictionary, not a set
print(empty_set) # output: set()

# Creating a set with duplicate values (duplicates are automatically removed)
set_with_duplicates : set = {1,2,3,4,5,2,3,4,4}
print(set_with_duplicates)

print("*********************")

# Adding & Removing Elements
# Adding elements 
my_set1 = {1,2,3}
my_set1.add(4)  # Add a single element
print("Add a single element: ",my_set1)

my_set1.update([5,6,7]) # add multiple elements
print("add multiple elements: ", my_set1)

print("*************************")

# Removing Elements

my_set2 = {"a","b","c","d","e"}
print(my_set2)
my_set2.remove("a") # Removes 3; raises an error if not found
print("a removed: ",my_set2)

# my_set2.discard("f") # Does not raise an error if element is not found
# print(my_set2)
my_set2.discard("d") # Does not raise an error if element is not found
print("d is removd:", my_set2)

popped_element = my_set2.pop() #Removes and returns an arbitrary element
print(popped_element)

print("*******************")
print("Clearing a Set:")
# Clearing a Set

my_set2.clear()
print("remove all elelements: ",my_set2)   # Removes all elements


print("*******************")
print("Set Operations:")

# Set Operations in Python
# Union (| or union())

A = {1,2,3}
B = {3,4,5}
print("A set elements: ",A)
print("B set elements: ",B)
print("A union B: ",A | B) # output: {1,2,3,4,5}
print("Same as above: ",A.union(B)) # same as above


print("*******************")
#Intersection (& or intersection())
# Finds common elements between two sets.
A = {1,2,3}
B = {3,4,5}
print("A set elements: ",A)
print("B set elements: ",B)
print("A interaction B: ",A & B) # output: {3}
print("same as above: ",A.intersection(B)) # Same as above

print("*********************")
#  Difference (- or difference())
# Finds elements present in one set but not the other.
A = {1,2,3}
B = {3,4,5}
print("A set elements: ",A)
print("B set elements: ",B)
print("A difference B: ", A - B) #output: {1, 2}
print("Same as above:", A.difference(B))

print("*************************")

# Symmetric Difference (^ or symmetric_difference())
# Finds elements present in either of the sets but not both.

A = {1,2,3}
B = {3,4,5}
print("A set elements: ",A)
print("B set elements: ",B)

print("A Symmetric Difference B: ", A ^ B) #Output: {1,2,4,5}
print("A Symmetric Difference B: ", A.symmetric_difference(B))


print("********************************")

# Checking Subset, Superset, and Disjoint Sets
x = {1, 2}
y = {1, 2, 3, 4}

print("x is subset of y:",x.issubset(y)) # True (x ⊆ y)
print("see above, To decide y is superset of x: ",y.issuperset(x)) # True (y ⊇  x)

z = {5, 6}
print("x is disjoint to z: ",x.isdisjoint(z))  #True (No common elements)


print("*********************************")
# Converting Lists & Tuples to Sets
print("converting process start: ")
# Removing duplicates from a list
numbers  = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers) # Output: {1, 2, 3, 4, 5}


# Converting a set back to a list
unique_list = list(unique_numbers)
print("convert a set back to a list: ",unique_list)

print("********************************")


print("Hashing...")
#  Hashing Immutable Objects

sets = {10, 20, "hello", (1,2,3)}

print(sets)

for item in sets:
    print(f"hash({item}) = {hash(item)}")


print("*************************")
# Custom Hashing in Sets

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def __hash__(self):
        return hash((self.brand, self.model))

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

# creating a set of car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Toyota", "Camry") # same car, same hash
car3 = Car("Honda", "Civic")


car_set = {car1, car2, car3}
print(len(car_set)) # Output: 2 (because car1 and car2 are equal


print("******************************")
"""
The id() function in Python returns the memory address of an object.
Since sets store unique objects based on their hash values, id() helps us understand how Python handles object storage in sets.
"""

#  id() with Sets
mysets = {10, "Hello", 20, "World", 30}

print("Set Elements and their IDs: ")
for items in mysets:
    print(f"{items} -> id: {id(items)}")


print("****************************")


class Cars:
    def __init__(self, brand):
        self.brand = brand
        # self.model = model
    
    def __hash__(self):
        return hash((self.brand))  # Hash based on brand

    def __eq__(self, other):
        return isinstance(other, Cars) and self.brand == other.brand 

# creating a set of car objects
car1 = Cars("Toyota")
car2 = Cars("Toyota") # same brand, but difference objects
car3 = Cars("Honda")


car_set = {car1, car2, car3}
print("\nCar Objects and their IDs:")
for car in car_set:
    print(f"{car.brand} -> id: {id(car)}")

print("****************************")
"""
A frozenset is an immutable version of a Python set. Unlike normal sets, which are mutable (changeable), frozenset cannot be modified after creation.

✅ Key Features of frozenset:

Immutable (cannot add/remove elements)
Hashable (can be used as a dictionary key or stored in another set)
Supports set operations (union, intersection, difference, etc.)
"""

normal_set = {1, 2, 3, 4, 5}

# converting to a frozenset
frozen = frozenset(normal_set)

print("frozenset: ", frozen)
print("type: ", type(frozen))

