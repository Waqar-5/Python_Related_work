class Example:
     # __new__ is a static method that creates the object
    def __new__(cls, *args, **kwargs):
        print("Step 1: __new__ is called - Creating instance")
        instance = super().__new__(cls)  # Actually create the instance
        return instance
        # return super().__new__(cls)


    #  __init__ initializes the object after it's created
    def __init__(self, value):
        print("Step 2: __init__ is called - Initializing instance")
        self.value  = value

        # __del__ is called when the object is about to be destroyed
    def __del__(self):
         print(f"Step 3: __del__ is called - Cleaning up instance with value {self.value}")



obj = Example(45)
print(f"Object's value: {obj.value}")

# Delete the object explicitly to trigger __del__
del obj


# Note: __del__ may also run automatically when program ends or object is garbage collected.
# Step 1: __new__ is called - Creating instance   # Object memory allocated
# Step 2: __init__ is called - Initializing instance  # Object initialized with value
# Object's value: 42
# Step 3: __del__ is called - Cleaning up instance with value 42  # Object destroyed/cleaned



print("*************************")

# Base class: Vehicle
class Vehicle:
    # Constructor: Called when an object is created
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"[Vehicle __init__] Created Vehicle: {self.brand} {self.model}")

    # Destructor: Called when an object is destroyed
    def __del__(self):
        print(f"[Vehicle __del__] Destroying Vehicle: {self.brand} {self.model}")

   # Method to display vehicle info

    def display_info(self):
        print(f"Vehicle Info: {self.brand} {self.model}")

    
# Subclass: Car inherits from Vehicle

class Car(Vehicle):
     # Override constructor to add more attributes
    def __init__(self, brand, model, doors):
        # Call the base class constructor
        super().__init__(brand, model)
        self.doors = doors
        print(f"[Car __init__] Added doors: {self.doors}")

 # Override destructor to add custom cleanup

    def __del__(self):
        print(f"[Car __del__] Destroying Car: {self.brand} {self.model} with {self.doors} doors")
        # Optionally call parent destructor explicitly (not required, but good practice)
        super().__del__()

    
    # Method specific to Car
    def display_car_info(self):
        print(f"Car: {self.brand} {self.model}, Doors: {self.doors}")

# Create a Car object
my_car = Car("Toyota", "Corolla", 4)

# Use methods
my_car.display_info()      # From Vehicle class
my_car.display_car_info()  # From Car class

# Delete the object explicitly to call destructor immediately (optional)
del my_car