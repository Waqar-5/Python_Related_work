# Everything in Python is an object: numbers, functions, classes.

# This allows great flexibility and uniform handlin

# Python’s Unified Type System – Detailed Explanation


"""
Everything is an Object
All values and entities in Python are instances of some class. Even simple data types like int, float, and str are class instances.
"""
# Numbers are objects
x = 10
print(type(x))           # <class 'int'>
print(x.bit_length())    # Method of int objects

# Strings are objects
s = "hello"
print(type(s))           # <class 'str'>
print(s.upper())         # Method of str objects


print("******************************")

#  Functions are Objects
# Functions can be assigned to variables, passed as arguments, and stored in data structures, just like any other object.
def greet(name):
    return f"Hello, {name}!"

# Assigning function to a variable
say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# Functions have attributes
print(greet.__name__)      # greet

print("******************************")

"""
Classes are Objects
In Python, classes themselves are instances of the type class.
"""
class MyClass:
    pass

print(type(MyClass))       # <class 'type'> -> MyClass is an object too
obj = MyClass()
print(type(obj))           # <class '__main__.MyClass'>

print("******************************")

"""
Modules are Objects
Even imported modules are objects.
"""

import math

print(type(math))          # <class 'module'>
print(math.sqrt(16))       # 4.0

print("******************************")


"""
Objects Can Be Inspected Uniformly
Since everything is an object, Python provides reflection and introspection tools like dir() and type() to inspect objects.
"""

print(dir(5))              # Lists attributes/methods of int
print(dir(str))            # Lists methods of str class
print(dir(len))            # len is a function (also an object)


print("******************************")




"""
 Custom Object Demonstrating Uniformity
Here’s a class that behaves like a number using magic methods:
"""
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __str__(self):
        return str(self.value)

# Custom number objects
a = MyNumber(10)
b = MyNumber(20)
c = a + b
print(c)         # 30
print(type(c))   # <class '__main__.MyNumber'>

print("******************************")
# Python App Demonstrating Unified Type System
# Everything in Python is an object: numbers, functions, classes, modules, etc.

# --- Custom Number Class to Mimic int Behavior ---

class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        return NotImplemented
    
    def __str__(self):
        return f"MyNumber({self.value})"
    
    def __repr__(self):
        return str(self)
    
# --- Function Object Example ---
def greet(name):
    return f"Hello, {name}!"

# Assign function to another variable (functions are objects)
alias_greet = greet

# --- Module Example ---
import math

def module_info(mod):
    print(f"Module Name: {mod.__name__}")
    print(f"Type of module: {type(mod)}")
    print(f"Square root of 25: {mod.sqrt(25)}")



# --- Introspection Example ---
def introspect(obj):
    print(f"Object: {obj}")
    print(f"Type: {type(obj)}")
    print(f"Attributes/Methods: {dir(obj)}\n")



# --- Unified Object App Execution ---
if __name__ == "__main__":
    print("--- Custom Number Objects ---")
    a = MyNumber(10)
    b = MyNumber(20)
    c = a + b
    print(f"a: {a}, b: {b}, a + b = c: {c}")

    print("\n--- Function Object Demo ---")
    print(alias_greet("Alice"))  # Calls the same function through alias
    print(f"Function name: {greet.__name__}")

    print("\n--- Module Object Demo ---")
    module_info(math)  # math module is also an object

    print("\n--- Introspection Demo ---")
    introspect(42)           # int
    introspect("Hello")      # str
    introspect(greet)        # function
    introspect(MyNumber)     # class
    introspect(a)            # object instance


print("**********************")
# 🌟 Beautiful Python App Showcasing Unified Type System 🌟
# Everything in Python is an object: numbers, functions, classes, modules, etc.
# This app uses print styling and separators to make output more attractive and readable.

# --- 🎯 Custom Number Class to Mimic int Behavior ---
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        return NotImplemented

    def __str__(self):
        return f"MyNumber({self.value})"

    def __repr__(self):
        return str(self)

# --- 💬 Function Object Example ---
def greet(name):
    return f"Hello, {name}!"

# Functions are objects and can be assigned to other variables
alias_greet = greet

# --- 📦 Module Object Example ---
import math

def module_info(mod):
    print("\n🔍 Module Information")
    print("=" * 40)
    print(f"📛 Name: {mod.__name__}")
    print(f"📦 Type: {type(mod)}")
    print(f"🧮 sqrt(25): {mod.sqrt(25)}")
    print("=" * 40)

# --- 🔎 Introspection Tool ---
def introspect(obj):
    print("\n🔍 Introspection")
    print("=" * 40)
    print(f"🆔 Object: {repr(obj)}")
    print(f"🔤 Type: {type(obj)}")
    print(f"🔧 Attributes/Methods (partial list):")
    attrs = dir(obj)
    print("  ", ", ".join(attrs[:8]) + ", ...")  # Only show first few for brevity
    print("=" * 40)

# --- 🚀 App Execution ---
if __name__ == "__main__":
    print("\n🌟 WELCOME TO PYTHON UNIFIED TYPE SYSTEM DEMO 🌟")
    print("=" * 60)

    print("\n🧮 Custom Number Class Demo")
    a = MyNumber(10)
    b = MyNumber(20)
    c = a + b
    print(f"✅ a = {a}")
    print(f"✅ b = {b}")
    print(f"🔢 a + b = c → {c}")

    print("\n💡 Function Object Demo")
    print(f"✅ alias_greet('Alice') → {alias_greet('Alice')}")
    print(f"🔤 Original function name: {greet.__name__}")

    module_info(math)  # Display info about math module

    print("\n🧠 Introspection Demos")
    introspect(42)           # int
    introspect("Hello")      # str
    introspect(greet)        # function
    introspect(MyNumber)     # class
    introspect(a)            # object instance

    print("\n✨ Thank you for exploring Python's Unified Type System! ✨")