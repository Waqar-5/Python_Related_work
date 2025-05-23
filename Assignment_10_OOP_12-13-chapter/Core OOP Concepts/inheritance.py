# Single Inheritance
# 👨 Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    # 🐶 Child Class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks: Woof!")

    
# 🎯 Creating object of Dog
dog1 = Dog("Buddy")

# 🔁 Accessing methods from both Parent and Child class
dog1.speak()   # Inherited from Animal
dog1.bark()    # Defined in Dog

print("**************************")


# Multiple Inheritance
# 🍎 First Parent
class Fruit:
    def fruit_info(self):
        print("I am a Fruit.")

# 🥦 Second Parent
class Vegetable:
    def vegetable_info(self):
        print("I am a Vegetable.")


# 🥗 Child inherits from both Fruit and Vegetable
class Salad(Fruit, Vegetable):
    def mix(self):
        print("Mixing fruits and vegetables!")

# 🎯 Create a Salad object
s = Salad()
s.fruit_info()       # From Fruit class
s.vegetable_info()   # From Vegetable class
s.mix()              # From Salad class



print("****************************************")


# . Using super() in Inheritance

# 👴 Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

# 👦 Child Class
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # Calls Person's constructor
        self.grade = grade

    def show(self):
        super().show()  # Calls Person's show() method
        print(f"Grade: {self.grade}")

# 🎯 Create object
s1 = Student("Ali", "A+")
s1.show()

print('****************************************')

# 1. Single Inheritance

# 👨 Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# 🐶 Child Class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks: Woof!")

# 🎯 Creating object of Dog
dog1 = Dog("Buddy")

# 🔁 Accessing methods from both Parent and Child class
dog1.speak()   # Inherited from Animal
dog1.bark()    # Defined in Dog
print("**************************")
# Multiple Inheritance
# 🍎 First Parent
class Fruit:
    def fruit_info(self):
        print("I am a Fruit.")

# 🥦 Second Parent
class Vegetable:
    def vegetable_info(self):
        print("I am a Vegetable.")

# 🥗 Child inherits from both Fruit and Vegetable
class Salad(Fruit, Vegetable):
    def mix(self):
        print("Mixing fruits and vegetables!")

# 🎯 Create a Salad object
s = Salad()
s.fruit_info()       # From Fruit class
s.vegetable_info()   # From Vegetable class
s.mix()              # From Salad class

print("****************************************")

# Multilevel Inheritance
# 👴 Grandparent Class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# 👨 Parent Class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof!")

# 👶 Child Class (inherits from Dog)

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps softly...")


# 🎯 Create an object of the lowest level
p = Puppy()

# access all methods from three levels
p.sound() # From Animal
p.bark()   # From Dog
p.weep()   # From Puppy
print("****************************************")

# Hierarchical Inheritance

# 👨 Parent Class
class Vehicle:
    def start(self):
        print("Vehile is starting...")

# 🚗 Child Class 1 (inherits from Vehicle)
class Car(Vehicle):
    def drive(self):
        print("Car is driving...")

# 🏍️ Child Class 2 (inherits from Vehicle)
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding...")

# 🎯 Create objects of both child classes
c = Car()
b = Bike()

# ✅ Each child can use parent methods
c.start()
c.drive()

b.start()
b.ride()
print("****************************************")


# Hybrid Inheritance (Combination of Multiple and Multilevel)

# 🔹 Base Class
class Person:
    def who_am_i(self):
        print("I am a person.")

# Parent 1
class Teacher(Person):
    def teach(self):
        print("I teach students.")

# Parent 2
class Student(Person):
    def study(self):
        print("I study hard.")

# 👨‍🎓 Child Class inherits from both Teacher and Student
class TeachingAssistant(Teacher, Student):
    def assist(self):
        print("I assist in teaching and studying.")

# 🎯 Create an object of TeachingAssistant
ta = TeachingAssistant()

# use all inherited methods
ta.who_am_i()
ta.teach()
ta.study()
ta.assist()

print("****************************************")

# using five types of inheritance in this exmaple
from colorama import init, Fore, Style
# Initialize colorama (needed for Windows)
init(autoreset=True)

# 🔰 Base Class
class Person:
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(Fore.CYAN + f"👤 I am {self.name}, a person at this school.")

# ----------------------------
# 🧬 SINGLE INHERITANCE
class Teacher(Person):
    def teach(self):
        print(Fore.YELLOW + f"👩‍🏫 {self.name} teaches a class.")


   # ----------------------------
# 🧬 MULTILEVEL INHERITANCE

class Student(Person):
    def study(self):   print(Fore.GREEN + f"📚 {self.name} is studying.")

class SeniorStudent(Student):
    def lead_group(self):
        print(Fore.LIGHTBLUE_EX + f"👨‍🎓 {self.name} leads a study group.")


# ----------------------------
# 🧬 HIERARCHICAL INHERITANCE
class Staff(Person):
    def maintain(self):
        print(Fore.MAGENTA + f"🧑‍💼 {self.name} maintains the school building.")


# ----------------------------
# 🧬 MULTIPLE + HYBRID INHERITANCE
class Assistant(Teacher, Student):
    def assist(self):
        print(Fore.LIGHTCYAN_EX + f"🧑‍💻 {self.name} assists both teaching and learning.")



# 🎮 MAIN FUNCTION
def main():
     print(Style.BRIGHT + Fore.BLUE + "\n🎓 Welcome to the Smart School System 🎓\n")



  # 💡 Take names from user
# teacher_name = input("👩‍🏫 Enter teacher's name: ")
# student_name = input("📚 Enter senior student's name: ")
# staff_name = input("🧹 Enter staff member's name: ")
# assistant_name = input("🧑‍💻 Enter assistant's name: ")




# 
# 👩‍🏫 Teacher (Single Inheritance)
#t = Teacher(teacher_name)
t = Teacher("Asad")
t.who_am_i()
t.teach()
print(Fore.WHITE + "─" * 50)
# print("\n" + Style.DIM + Fore.YELLOW + "-------------------------------------\n")


# 📚 Senior Student (Multilevel Inheritance)
ss = SeniorStudent("Ali")
#   ss = SeniorStudent(student_name)
ss.who_am_i()
ss.study()
ss.lead_group()
print(Fore.WHITE + "─" * 50)


# 🧹 Staff (Hierarchical Inheritance)
s = Staff("Mr. Ameer")
s.who_am_i()
s.maintain()
print(Fore.WHITE + "─" * 50)

# 🧑‍💻 Assistant (Multiple + Hybrid Inheritance)
# 🧑‍💻 Assistant (Hybrid Inheritance)

a = Assistant("Sameer")
a.who_am_i()
a.teach()
a.study()
a.assist()
print(Fore.WHITE + "─" * 50)



print(Style.BRIGHT + Fore.GREEN + "✅ All 5 Inheritance Types Demonstrated Successfully!")

# 🔁 Run the app
if __name__ == "__main__":
    main()