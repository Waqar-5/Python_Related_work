# Composition (Strong "has-a" relationship)

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} PH started.")

class Car:
    def __init__(self, make, horsepower):
        self.make = make
    #creating an Engine object inside Car: Compostion
        self.engine = Engine(horsepower)
    
    def drive(self):
        print(f"{self.make} car is driving...")
        self.engine.start()


# Create a car
my_car = Car("Toyota", 150)
my_car.drive()

# The Engine object is part of the Car ob

"""
 Key Points:
Car owns Engine → strong relationship.

Engine is created inside the Car class.

When the Car object is deleted, its Engine is deleted too.

This is Composition.
"""

print("*****************************")


# Aggregation (Weaker "has-a" relationship)

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} PH started.")

class Car:
    def __init__(self, make, engine):
        self.make = make
           # Engine is passed as an argument: Aggregation
        self.engine = engine

    def drive(self):
        print(f"{self.make} car is driving...")
        self.engine.start()


   # Create an engine independently
external_engine = Engine(200)

# Create multiple cars that share the same engine
car1 = Car("Honda", external_engine)
car2 = Car("Ford", external_engine)

car1.drive()
car2.drive()

# Engine still exists even if cars are deleted
del car1
print("car1 deleted")
external_engine.start()  # Engine is still usable     

"""
Engine is created outside of Car and passed in → Aggregation.

Engine is not owned by Car, just used by it.

Even if Car is deleted, the Engine can still be used.

This is a weaker relationship than Composition.
"""

print("***************************")

# 🚗 Vehicle Manager App (Composition vs Aggregation)

import time

# Terminal colors for styling
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#  Engine class -used by car
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"{Colors.OKGREEN}Engine with {self.horsepower} HP started.{Colors.ENDC}")


# Car class demonstrating Composition
class CarComposition:
    def __init__(self, make, horsepower):
        self.make = make
        # Engine created inside - Composition
        self.engine = Engine(horsepower)

    def drive(self):
        print(f"{Colors.OKBLUE}{self.make} (Composition) car is driving...{Colors.ENDC}")
        self.engine.start()


# Car class demonstrating Aggregation
class CarAggregation:
    def __init__(self, make, engine):
        self.make = make
         # Engine passed externally - Aggregation
        self.engine = engine

    def drive(self):
        print(f"{Colors.OKCYAN}{self.make} (Aggregation) car is driving...{Colors.ENDC}")
        self.engine.start()


# main app
def main():
    print(f"{Colors.HEADER}{Colors.BOLD}Welcome to Vehicle Manager App! 🚗{Colors.ENDC}\n")
    time.sleep(1)

    shared_engines = []  # Store engines for aggregation
    cars_composition = []  # Store cars created with composition

    while True:
              print(f"""
{Colors.BOLD}Choose an option:{Colors.ENDC}
1. Create a Car (Composition)
2. Create an Engine for Aggregation (shared engine)
3. Create a Car (Aggregation) using shared engine
4. Drive all Cars
5. Exit
""")
              choice = input(f"{Colors.WARNING}Enter choice: {Colors.ENDC}")
              
              if choice == "1":
                make = input("Enter Car make (Composition): ")
                hp = int(input("Enter Engine horsepower: "))
                car = CarComposition(make, hp)
                cars_composition.append(car)
                print(f"{Colors.OKGREEN}Car with Composition created successfully!{Colors.ENDC}\n")
              
              elif choice == "2":
                hp = int(input("Enter Engine horsepower for shared engine: "))
                engine = Engine(hp)
                shared_engines.append(engine)
                print(f"{Colors.OKGREEN}Shared Engine created successfully!{Colors.ENDC}\n")

              elif choice == "3":
                if not shared_engines:
                 print(f"{Colors.FAIL}No shared engines available! Create one first.{Colors.ENDC}\n")
                 continue
                print("Available shared engines:")
                for idx, eng in enumerate(shared_engines):
                    print(f"{idx+1}. Engine with {eng.horsepower} HP")
                idx = int(input("Select engine number to use: ")) - 1
                if idx < 0 or idx >= len(shared_engines):
                    print(f"{Colors.FAIL}Invalid selection!{Colors.ENDC}\n")
                    continue
                make = input("Enter Car make (Aggregation): ")
                car = CarAggregation(make, shared_engines[idx])
                cars_aggregation.append(car)
                print(f"{Colors.OKGREEN}Car with Aggregation created successfully!{Colors.ENDC}\n")

              elif choice == "4":
                print(f"{Colors.BOLD}Driving all cars...{Colors.ENDC}\n")
                if not cars_composition and not cars_aggregation:
                    print(f"{Colors.WARNING}No cars to drive! Create some first.{Colors.ENDC}\n")
                for car in cars_composition:
                    car.drive()
                for car in cars_aggregation:
                    car.drive()
                print()
                time.sleep(1)

              elif choice == "5":
                print(f"{Colors.HEADER}Thanks for using Vehicle Manager App! Goodbye! 👋{Colors.ENDC}")
                break
              else:
                print(f"{Colors.FAIL}Invalid choice! Please select from 1-5.{Colors.ENDC}\n")


# Lists to hold cars
cars_composition = []
cars_aggregation = []

if __name__ == "__main__":
    main()

                  
        


