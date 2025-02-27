# Data types
#  1. Numeric Types
# => Integer(int) whole numbers without decimal points.
# => Float(float) numbers with decimal points.
# => complex(complex)  numbers with real and imaginary parts.

x : int = 10     # integer
y : float = 3.14     # float
z : complex = 2 + 3j    # complex

print(type(x))
print(type(y))
print(type(z))


print("***************************")

# 2. Sequence Types
""" These Data types store multiple values in an ordered manner.
String (str) => A sequence of characters enclosed in quotes

List(list) => A mutable (modifiable) ordered collection of elements.


Tuple (tuple) => An immutable (unchangeable) ordered collection of elements.

Range (range) => A sequence of numbers used in loops.
"""
# Examples

s = "Hello, Welcome in coding!"  # String
l = [1, 2, 3, 4, 5]              # List
t = (5, 6, 7, 8, 9)              # Tuple
r = range(1, 7)                   # Range

print(type(s))
print(type(l))
print(type(t))
print(type(r))

print("*******************************")
# 3. Boolean Type
# A boolean(bool) typee represents True or False values

a = True
b = False

print(type(a))
print(type(b))



# Set Types => A set an unordered collection of unique items.
"""
Set (set) => A mutable collection of unique elements.

FrozenSet(frozenset) => An immutable version of a set.
"""

s1 = {1, 2, 3, 4}
s2 = frozenset([5, 6, 7])

print(type(s1))
print(type(s2))

print("******************************")

# Dictionary Types(dict) => Store key-value pairs
# A collection of key-value pairs.

d = {"name" : "Ali", "age" : 25, "city" : "Karachi"}	
print(type(d))

print("******************************")


# Binary Types => Bytes and Bytearray
# Bytes(bytes) => Immutable sequence of bytes.
# Bytearray(bytearray) => Mutable sequence of bytes.
#Memoryview(memoryview) => Read-only view of a bytes object/ Allows viewing memory of objects.

b = b"Hello"
ba = bytearray(b)
mv = memoryview(b)

print(type(b))
print(type(ba))


print("******************************")

