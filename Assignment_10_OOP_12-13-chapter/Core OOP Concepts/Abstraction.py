# 11. Abstraction
# Hide complex implementation details behind simple interfaces.

# Achieved using Abstract Base Classes (abc module).

# Abstract classes have abstract methods which must be implemented by subclasses.

# Example:
from abc import ABC, abstractmethod

## Step 1: Create an abstract class
class Animal(ABC):
     # Abstract method (no body, must be implemented by subclasses)
    @abstractmethod
    def make_sound(self):
          pass
      # Concrete method (optional: shared behavior across all subclasses)
    def sleep(self):
        print("Sleeping... Zzz") 


# Step 2: Create a subclass that inherits from the abstract class
class Dog(Animal):
      # Implement the abstract method
    def make_sound(self):
         print("Bark!")

class Cat(Animal):
     # Implement the abstract method
    def make_sound(self):
         print("Meow!")


# Step 3: Instantiate the subclasses and use their methods
dog = Dog()
dog.make_sound()  # Output: Bark!
dog.sleep()       # Output: Sleeping... Zzz

cat = Cat()
cat.make_sound()  # Output: Meow!
cat.sleep()       # Output: Sleeping... Zzz

# 🚫 Trying to instantiate the abstract class directly will raise an error:
# animal = Animal()  # TypeError: Can't instantiate abstrac