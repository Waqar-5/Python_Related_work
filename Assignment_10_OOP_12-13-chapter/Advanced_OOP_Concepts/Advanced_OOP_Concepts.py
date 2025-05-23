# Metaclasses: Classes of classes; control class creation.

# Singleton pattern: Ensure only one instance of a class.

# Factory pattern: Create objects dynamically

"""
Metaclasses: Classes of Classes; Control Class Creation
A metaclass controls the creation of classes themselves. In Python, type is the default metaclass. You can create your own metaclass by inheriting from type and overriding its methods like __new__ or __init__ to customize class creation.
"""


# Define a custom metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
         # This method is called before the class is created
        print(f"Creating class {name} with MyMeta metaclass")

        # Add a custom attribute to the class dynamically
        dct['custom_attr'] = 'Added by MyMeta'

          # Create the class object using super() call to type.__new__
        return super().__new__(cls, name, bases, dct)
    
# Define a class with the metaclass MyMeta
class MyClass(metaclass = MyMeta):
    def __init__(self):
        print(f"MyClass instance created")

# When MyClass is defined, MyMeta.__new__ is triggered
print(MyClass.custom_attr)  # Access the dynamically added attribute

obj = MyClass()  # Create instance of MyClass  


print("*******************************")


#  Singleton Pattern: Ensure Only One Instance of a Class
# The Singleton pattern ensures that a class has only one instance throughout the application.

# Singleton metaclass
class SingletonMeta(type):
    _instances = {} # Dictionary to store one instance per class

    def __call__(cls, *args, **kwargs):
         # Check if instance already exists
        if cls not in cls._instances:
             # If not, create one and store it
            cls._instances[cls] = super().__call__(*args, **kwargs)
    # Return the stored instance
        return cls._instances[cls]

   # Class using SingletonMeta metaclass 
class SingletonClass(metaclass = SingletonMeta):
    def __init__(self, value):
        self.value = value


# Test
obj1 = SingletonClass(10)
obj2 = SingletonClass(20)

print(obj1.value)  # Output: 10
print(obj2.value)  # Output: 10
print(obj1 is obj2)  # Output: True, both refer to the same instance

print("*********************************")


# Factory Pattern: Create Objects Dynamically
# The Factory pattern provides an interface to create objects but lets subclasses or a separate factory class decide which class to instantiate.

# Base class for products
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
 

# Concrete product classes
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    

# Factory class to create objects dynamically

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Ünknown animal type")
        

# usage 
animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Output: Woof!

animal2 = AnimalFactory.create_animal("cat")
print(animal2.speak())  # Output: Meow!


print("**************************")


from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

# --- Metaclass example ---

class DemoMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_by_meta'] = "This attribute is added by DemoMeta"
        return super().__new__(cls, name, bases, dct)

class MetaDemoClass(metaclass=DemoMeta):
    def hello(self):
        return "Hello from MetaDemoClass instance!"

def run_metaclass_demo():
    console.rule("[bold cyan]Metaclass Demo[/bold cyan]")
    console.print("When this class was created, the metaclass added an attribute:")
    console.print(f"[bold green]MetaDemoClass.added_by_meta:[/bold green] {MetaDemoClass.added_by_meta}")
    instance = MetaDemoClass()
    console.print("Calling method from instance:")
    console.print(f"[bold yellow]{instance.hello()}[/bold yellow]")
    console.print("This shows how metaclasses can modify classes at creation time.\n")


# --- Singleton example ---

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonDemo(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

def run_singleton_demo():
    console.rule("[bold magenta]Singleton Pattern Demo[/bold magenta]")
    obj1 = SingletonDemo("First Instance")
    obj2 = SingletonDemo("Second Instance - Attempt to overwrite")
    
    console.print("Created two objects of SingletonDemo class:")
    console.print(f"obj1.value: [bold cyan]{obj1.value}[/bold cyan]")
    console.print(f"obj2.value: [bold cyan]{obj2.value}[/bold cyan]")
    console.print(f"obj1 is obj2? [bold yellow]{obj1 is obj2}[/bold yellow]")
    console.print("This shows only one instance is created and shared.\n")


# --- Factory Pattern example ---

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        elif animal_type == "bird":
            return Bird()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

def run_factory_demo():
    console.rule("[bold green]Factory Pattern Demo[/bold green]")
    console.print("Available animals: dog, cat, bird")
    animal_type = Prompt.ask("Enter an animal type")
    try:
        animal = AnimalFactory.create_animal(animal_type)
        console.print(f"[bold cyan]{animal_type.capitalize()} says:[/bold cyan] [yellow]{animal.speak()}[/yellow]")
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
    console.print()


# --- Main app loop ---

def main():
    console.print(Panel.fit("[bold underline]Advanced OOP Concepts Demo[/bold underline]\n"
                            "Metaclasses | Singleton Pattern | Factory Pattern\n", style="bright_blue"))
    
    while True:
        console.print("Select a concept to explore:\n"
                      "1. Metaclasses\n"
                      "2. Singleton Pattern\n"
                      "3. Factory Pattern\n"
                      "4. Exit\n")
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"])
        
        if choice == "1":
            run_metaclass_demo()
        elif choice == "2":
            run_singleton_demo()
        elif choice == "3":
            run_factory_demo()
        else:
            console.print("[bold red]Exiting... Thanks for exploring![/bold red]")
            break

if __name__ == "__main__":
    main()
