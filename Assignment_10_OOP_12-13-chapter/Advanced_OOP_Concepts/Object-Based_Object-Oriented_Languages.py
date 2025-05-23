# Object-based: Support objects but no inheritance or polymorphism.

# Object-oriented: Support inheritance, polymorphism, encapsulation fully.

# Python is fully object-oriented.


# ---------------------------------------------
# Object-Based vs. Object-Oriented Explanation
# ---------------------------------------------

# Object-Based:
# Supports objects and encapsulation but not inheritance or polymorphism.
# Example below imitates object-based style.

print("🔷 Object-Based Style Example")

class Car:
    def __init__(self, model):
        self.model = model
    
    def start(self):
        print(f"{self.model} is starting.")

my_car = Car("Toyota")
my_car.start()
# Note: No inheritance or polymorphism used here.

print("\n🔷 Now demonstrating Python's full Object-Oriented support\n")

# ---------------------------------------------
# Python is Fully Object-Oriented
# ---------------------------------------------
# Supports:
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction (via abc module)

# 1. Encapsulation
print("✅ 1. Encapsulation Example")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Ali", 1000)
account.deposit(500)
print(f"{account.owner}'s balance: {account.get_balance()}")

# 2. Inheritance
print("\n✅ 2. Inheritance Example")
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

dog = Dog()
print(f"Dog says: {dog.speak()}")

# 3. Polymorphism
print("\n✅ 3. Polymorphism Example")
class Bird:
    def fly(self):
        print("Bird flying high!")

class Plane:
    def fly(self):
        print("Plane flying with engines!")

def start_flight(flyable):
    flyable.fly()

start_flight(Bird())   # Bird flying high!
start_flight(Plane())  # Plane flying with engines!

# 4. Abstraction
print("\n✅ 4. Abstraction Example (using abc module)")
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

vehicle = Car()
vehicle.start_engine()

# ---------------------------------------------
# Summary
# ---------------------------------------------
print("\n✅ Python is a Fully Object-Oriented Language!")
print("Supports: Encapsulation, Inheritance, Polymorphism, Abstraction")
