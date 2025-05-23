# 10. Polymorphism
# Same method name behaves differently in different classes.

# Method overriding: Child class provides its own method implementation.

# Operator overloading: Customize behavior of operators like +.

# Duck typing: If it looks like a duck and quacks like a duck, it’s a duck (focus on behavior, not type).

# Polymorphism Example in Python


# . Method Overriding
class Animal:
    def sound(self):
        print("Some generic animal sound")
        # return "Some generic animal sound"
    
class Dog(Animal):
    def sound(self):
        print("Bark!")
        # return "Bark!"

class Cat(Animal):
    def sound(self):
        print("Meow!")
        # return "Meow!"


#  Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
       # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses the overloaded + operator

print(p3)  # Output: (4, 6)

print("***********************************")


# Duck Typing

class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I can imitate a duck: Quack!")

def make_it_quack(thing):
    thing.quack()

d = Duck()
p = Person()

make_it_quack(d)  # Quack! Quack!
make_it_quack(p)  # I can imitate a duck: Quack!

print("*********************************")


# create objects
a = Animal()
d = Dog()
c = Cat()

# call the sound method
a.sound()  # Output: Some generic animal sound
d.sound()  # Output: Bark!
c.sound()  # Output: Meow!



# 1. Method Overriding: Different animals make different sounds
class Animal:
    def sound(self):
        return "Some generic animal sound"
    
class Dog(Animal):
    def sund(self):
        return "Bark!"
    

class Cat(Animal):
    def sund(self):
        return "Meow!"
    
# 2. Operator Overloading: Adding two Points
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y  

    def __add__(self, other):
        return Point(self.x + self.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"



# 3. Duck Typing: Any object with a 'quack' method is treated like a duck
class Duck:
    def quack(self):
        return "Quack! Quack!"
    

class Person:
    def quack(self):
        return "I can imitate a duck: Quack!"
    
def make_it_quack(thing):
    print(thing.quack())

# using method overriding
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

print("---")

# Using Operator Overloading
p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2) # output Point(6, 8)


print("---")
# Using Duck Typing
make_it_quack(Duck())
make_it_quack(Person())


print("******************************")
# 🐾 Polymorphism in Action 🐾

# 🧩 Method Overriding: Different animals speak differently
class Animal:
    def speak(self):
        return "🔈 Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "🐶 Bark! Bark!"

class Cat(Animal):
    def speak(self):
        return "🐱 Meow!"

class Cow(Animal):
    def speak(self):
        return "🐮 Moo!"

# ➕ Operator Overloading: Adding coordinates with style
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Custom behavior for +
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"📍 Vector({self.x}, {self.y})"

# 🦆 Duck Typing: If it quacks, it's a duck
class Duck:
    def quack(self):
        return "🦆 Quack! Quack!"

class Human:
    def quack(self):
        return "👨‍🦰 I can quack too! Quack!"

def make_it_quack(entity):
    # No type checking — just behavior!
    print(entity.quack())

# 🌈 Let's see polymorphism in action!

print("🔊 Method Overriding Demo:")
animals = [Dog(), Cat(), Cow(), Animal()]
for a in animals:
    print(f"➡️ {a.speak()}")

print("\n➕ Operator Overloading Demo:")
v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(f"🧮 Adding Vectors: {v1} + {v2} = {v1 + v2}")

print("\n🦆 Duck Typing Demo:")
make_it_quack(Duck())    # Quack from a Duck
make_it_quack(Human())   # Quack from a Human impersonator
