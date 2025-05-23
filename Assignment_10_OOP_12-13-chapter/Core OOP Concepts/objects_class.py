"""
Introduction to OOP
OOP (Object-Oriented Programming) is a programming style that organizes software design around objects rather than functions and logic.

Objects bundle data (attributes) and functions (methods) together.

This approach models real-world things, making programming more intuitive and manageable.



 What is OOP?
Definition: A programming paradigm based on the concept of “objects” which have attributes (data) and methods (functions).

Benefits:

Modularity: Code is divided into independent modules (classes).

Reusability: Classes can be reused across programs.

Maintainability: Easier to update or fix.

Scalability: Can grow with complexity.

Real-world modeling: Closer to how we see the world.

Key Principles of OOP
Encapsulation: Group data and methods inside classes, hiding internal details from outside.

Abstraction: Show only necessary features to the outside world, hide complexity.

Inheritance: Child classes inherit properties and behavior from parent classes.

Polymorphism: One interface, many forms; methods behave differently based on the object.


"""

# 4. Basics of Classes & Objects
# Class: Blueprint or template defining attributes and methods.

# Object: An instance of a class.

# self: Refers to the current object inside class methods.

# Instantiation: Creating an object from a class.


class Car:
    def __init__(self, model):
        self.model = model

my_car = Car("Toyota")  # my_car is an object (instance) of class Car
print(my_car.model)


# Define a class (template) for a Pet
class Pet:
      # Constructor method to initialize the object
    def __init__(self, name, animal_type, sound):
        self.name = name  # Name of the pet
        self.animal_type = animal_type  # Type of pet (e.g., Dog, Cat)
        self.sound = sound    # Sound the pet makes


    # Method to introduce the pet
    def introduce(self):
        print(f"Hi! I am {self.name}, and I am a {self.animal_type}.")

    # Method to make the pet speak
    def speak(self):
        print(f"{self.name} says: {self.sound}!")

    

# 🎉 Create objects (pets) from the Pet class
pet1 = Pet("Buddy", "Dog", "Woof")
pet2 = Pet("Mile", "Cat", "Meow")
pet3 = Pet("Chirpy", "Parrot", "Squawk")


# 🐾 Call methods on each object
pet1.introduce()  # Output: Hi! I am Buddy, and I am a Dog.
pet1.speak()     # Output: Buddy says: Woof!

pet2.introduce()  # Output: Hi! I am Mile, and I am a Cat.
pet2.speak()     # Output: Mile says: Meow!

pet3.introduce()  # Output: Hi! I am Chirpy, and I am a Parrot. 
pet3.speak()     # Output: Chirpy says: Squawk!



print('*****************************')


#  Example: "Student" Class — Only Classes and Objects
# define a class named Student
class Student:
        # Constructor method (__init__) is used to create and initialize the object
        def __init__(self, name, grade, roll_number):
              # 'self' refers to the current object being created
            self.name = name  # Store the student's name
            self.grade = grade  # Store the student's grade
            self.roll_number = roll_number  # Store the student's roll number

           # A method to display student's full details
        def show_details(self): 
               # Use object's data to print a formatted message
            print(f"Name: {self.name}, Grade: {self.grade}, Roll No: {self.roll_number}")

    # A method to greet the student

        def greet(self):
            print(f"Hello,{self.name}! Welcome to the class {self.grade}.") 

        
# 🧑‍🎓 Create objects (students) using the Student class
student1 = Student("Ali", "5th", 21)
student2 = Student("Ameer", "5th", 22)

# 🖨️ Call methods on each student object to show their data and greet them
student1.show_details() # Output: Name: Ayesha, Grade: 5th, Roll No: 21
student1.greet()         # Output: Hello, Ayesha! Welcome to the class 5th.

student2.show_details()  # Output: Name: Hamza, Grade: 5th, Roll No: 22
student2.greet()         # Output: Hello, Hamza! Welcome to the class 5th.


"""
💡 Key Concepts:
✅ Class: Blueprint (Student)

✅ Object: Instance (student1, student2)

✅ Attributes: name, grade, roll_number

✅ Methods: show_details(), greet()

✅ Constructor: __init__() initializes object data
"""


print("*****************************")



# Define a class named Student
class Student:
    # Constructor method: runs automatically when a new object is created
    def __init__(self, name, roll_no, grade):
        # 'self' refers to the current object
        self.name = name          # Store the student's name
        self.roll_no = roll_no    # Store the student's roll number
        self.grade = grade        # Store the student's grade

    # A method to display student details
    def display_info(self):
        # This prints the stored information of the student
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Grade:", self.grade)
        print("----------------------")

# ✅ Create objects (students) from the Student class
student1 = Student("Areeba", 101, "A")  # student1 is an object of Student
student2 = Student("Zayan", 102, "B")   # student2 is another object
student3 = Student("Iqra", 103, "A+")   # student3 is another object

# 🖨️ Call the display_info() method for each object to show their data
student1.display_info()
student2.display_info()
student3.display_info()

            


print("*********************")
# # 🎓 Define the Student class
class Student:
      # Constructor method to initialize each student's data
      def __init__(self, name, grade, roll_number):
          self.name = name
          self.grade = grade
          self.roll_number = roll_number

        
        # Method to show the student's information
      def show_info(self):
          print(f"Name: {self.name}, Grade: {self.grade}, Roll Number: {self.roll_number}")

 # Method to greet the student
      def greet(self):
          print(f"Hello, {self.name}! Welcome to the class {self.grade}.")

      # 📌 Ask how many students to add

num_students = int(input("How many students do you want to add? "))


# Create an empty list to store student objects
students_list = []

# ➕ Use a loop to take input and create student objects
for i in range(num_students):
    print(f"\nEnter details fr Student #{i + 1}")
    name = input("Enter name: ")
    grade = input("Enter grade (e.g., 5th): ")
    roll_number = input("Enter roll number: ")


 # Create a new Student object and add it to the list
    student = Student(name, grade, roll_number)
    students_list.append(student)  # Add the student object to the list


# 🖨️ Display info and greet each student
print(f"\n🎉 Student Records: ")
for student in students_list:
    student.show_info()  # Call the method to show info
    student.greet()      # Call the method to greet
    print("----------------------")