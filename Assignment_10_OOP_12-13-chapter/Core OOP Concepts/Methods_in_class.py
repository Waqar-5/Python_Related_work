# Instance Methods (Most Common)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self): # Instance method
        print(f"Student: {self.name}, Marks: {self.marks}")


# Create an object
s1 = Student("Ali", 90)
s1.display_info()  # Accessing instance method


print("***********************************")


#  2. Class Methods
class Student:
    school_name = "ABC School"  # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name  # Changing class attribute

# Call class method using class
Student.change_school("GIAIC")

print(Student.school_name)  # Output: Saylani 



#  Static Methods
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

print(Math.add(5, 3))  # Output: 8
print(Math.subtract(5, 3))  # Output: 2


# Code Example: Employee Class with All 3 Types of Methods

# Define a class named 'Employee'
class Employee:
    #class attribute: shared by all employees
    comapany_name = "TechCorp"

    # constructor: used to intialize the object's data
    def __init__(self, name, salary):
        self.name = name          # Instance attribute
        self.salary = salary      # Instance attribute

    #   # Instance Method: operates on specific object's data
    def show_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
        print(f"Salary: {self.salary}")
        print(f"Company Name: {Employee.comapany_name}") # Accessing class attribute

        # Class Method: modifies class-level data

    @classmethod
    def change_company(cls, new_name):
        cls.comapany_name = new_name  # Changing class attribute
        print(f"Company Name changed to: {cls.comapany_name}")

    # Static Method: utility method, no access to self or cls

    @staticmethod
    def working_hours():
        print("Working hours: 9 AM to 5 PM")

    
# Create instances (objects) of the Employee class
emp1 = Employee("Ali", 50000)
emp2 = Employee("Aliza", 65000)


# Call instance method to show object-specific details
emp1.show_details()  # Output: Employee Name: Ali, Salary: 50000
print("--------------------------------")
emp2.show_details()  # Output: Employee Name: Aliza, Salary: 65000


print("\n🔄 Changing company name using class method:\n")
# Call class method using class name
Employee.change_company("CodeZone")


# Show that the change affected all objects
print("\n🔁 Updated Details:")
emp1.show_details()
print("---------------")
emp2.show_details()

print("\n🕘 Display working hours using static method:")
# Call static method using class and object
Employee.working_hours()
emp1.working_hours()