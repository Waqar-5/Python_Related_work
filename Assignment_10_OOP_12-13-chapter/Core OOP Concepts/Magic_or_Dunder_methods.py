#  Special (Magic/Dunder) Methods
# Methods with double underscores to define behavior of operators and built-in functions.

# Examples: __init__, __str__, __add__, __len__.
#  __init__ → Constructor

class Person:
    def __init__(self, name, age):
        # This method initializes the object with name and age
        self.name = name
        self.age = age

# Creating an instance of Person class
person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

print("****************************")

# __str__ → String Representation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
          # This method returns a user-friendly string representation
        return f"{self.name} is {self.age} years old"

person1 = Person("Bob", 25)
print(person1)  # Output: Bob is 25 years old

print("*********************************")

# __add__ → Addition (+ operator)
# Defines behavior for the + operator.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        # This allows adding two BankAccount objects
        return BankAccount(self.balance + other.balance)

    def __str__(self):
        return f"Account balance: ${self.balance}"

acc1 = BankAccount(100)
acc2 = BankAccount(150)
acc3 = acc1 + acc2  # Calls __add__

print(acc3)  # Output: Account balance: $250

print("***************************")

#  __len__ → Length using len()

class BookShelf:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        # Returns number of books
        return len(self.books)

shelf = BookShelf(["Harry Potter", "Sherlock Holmes", "1984"])
print("Number of book: ",len(shelf))  # Output: 3

print("*****************************")


# __eq__ → Equality (== operator)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Checks if two points are equal
        return self.x == other.x and self.y == other.y

p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(4, 5)

print(p1 == p2)  # True
print(p1 == p3)  # False



# 🎨 ShapeMaster: A Geometry Toolkit using Magic Methods

import math

# Base class for all shapes
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    
    def __str__(self):
        return f"{self.name} (area: {self.area():.2f})"
    
    def __add__(self, other):
        # combine areas of two shapes
        return CombinedShape(self, other)
    
    def __qe__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __len__(self):
        # number of sides/edges
        return 0
    
# Circle class
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __len__(self):
        return 1  # You can consider circumference as 1 continuous edge


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __len__(self):
        return 4
    

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __len__(self):
        return 3


# Class to represent a combination of two shapes
class CombinedShape(Shape):
    def __init__(self, shape1, shape2):
        super().__init__("CombinedShape")
        self.shape1 = shape1
        self.shape2 = shape2

    def area(self):
        return self.shape1.area() + self.shape2.area()

    def __str__(self):
        return f"🔗 Combined: {self.shape1.name} + {self.shape2.name} (area: {self.area():.2f})"


# -----------------------
# 🎯 Demo / Showcase App
# -----------------------
if __name__ == "__main__":
    circle = Circle(5)
    rect = Rectangle(4, 6)
    tri = Triangle(3, 4)

    print("🟢", circle)
    print("🟥", rect)
    print("🔺", tri)
    print("")

    # Compare shapes
    print("🆚 Is circle > rectangle?", circle > rect)
    print("🆚 Is triangle == rectangle?", tri == rect)
    print("")

    # Add shapes
    combo = circle + rect
    print("➕ Combined shape:", combo)
    print("")

    # Use len()
    print(f"📏 Edges in circle: {len(circle)}")
    print(f"📏 Edges in triangle: {len(tri)}")
    print(f"📏 Edges in rectangle: {len(rect)}")


print("************************")


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def __repr__(self):
        # This helps developers understand the object at a glance
        return f"User(username='{self.username}', age={self.age})"

user = User("ali_coder", 21)
print(repr(user))  # Output: User(username='ali_coder', age=21)

print("*************************************")

# __lt__ → Less Than <
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        # Compares products based on price
        return self.price < other.price

p1 = Product("Pen", 10)
p2 = Product("Notebook", 20)

print(p1 < p2)  # Output: True


print("*******************************")

#  __gt__ → Greater Than >

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __gt__(self, other):
        # Compares students based on grade
        return self.grade > other.grade

s1 = Student("Sara", 85)
s2 = Student("Zain", 78)

print(s1 > s2)  # Output: True


print("***********************")

# __getitem__ → Indexing (obj[i])
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        # Allows index-based access
        return self.data[index]

my_list = MyList([10, 20, 30, 40])
print(my_list[2])  # Output: 30
print("****************************")

# __setitem__ → Assign with Index (obj[i] = value)
class MyList:
    def __init__(self, data):
        self.data = data

    def __setitem__(self, index, value):
        # Allows setting value at index
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]

my_list = MyList([1, 2, 3])
my_list[1] = 20
print(my_list[1])  # Output: 20

print("*********************************")
# __del__ → Destructor
class TempFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"File '{self.filename}' created.")

    def __del__(self):
        # Called when object is deleted or program ends
        print(f"File '{self.filename}' deleted.")

# Creating and deleting a file object
file = TempFile("test.txt")
del file  # Output: File 'test.txt' deleted.


