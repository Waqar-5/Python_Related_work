# Class Variables
class Dog:
    # cass varaibe
    species = "Canis Familiaris"

    def __init__(self, name):
        self.name = name # Instance variable


# Creating instnace
dog1 = Dog("Buddy")
dog2 = Dog("Max")


print(dog1.name)        # Buddy (instance-specific)
print(dog2.name)        # Max   (instance-specific)
print(dog1.species)     # Canis Familiaris (shared class variable)
print(dog2.species)     # Canis Familiaris

# Changing class variable via class
Dog.species = "Domestic Dog"

print(dog1.species)     # Domestic Dog
print(dog2.species)     # Domestic Dog

print("***********************************")

#  Static Methods

class MathUtility:
    @staticmethod
    def add(x, y):
        return x + y

# Call without creating an instance
result = MathUtility.add(5, 7)
print("Sum:", result)  # Output: Sum: 12


print("********************************")
# Class Methods

class Employee:
    company_name = "TechCrop"

    def __init__(self, name):
        self.name = name 

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

# Before changing
print(Employee.company_name) # TechCrop

# Using class method to change class variable
Employee.change_company("InnoTech")

# After changing
print(Employee.company_name)  # InnoTech


# 🌟 User Counter App (Pure OOP, Only Class Var, Static Method, Class Method)
import re

class User:
    # Class variable - shared by all users
    total_users = 0
    organization = "OpenAI"

    def __init__(self, name, email):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format!")
        
        self.name = name
        self.email = email

        # Increment user count
        User.total_users += 1
        print(f"✅ User '{self.name}' registered successfully.")

    @staticmethod
    def is_valid_email(email):

         """
         Static method to validate email format.
         Doesn't use class or instance data.
         """
         pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
         return re.match(pattern, email) is not None
    
    @classmethod
    def change_organization(cls, new_org):
          
          """
            Class method to change the shared organization name.
            """
          print(f"🔄 Changing organization from '{cls.organization}' to '{new_org}'")
          cls.organization = new_org

    def user_info(self):
        """
        Returns formatted info about the user.
        """
        return f"👤 Name: {self.name}, Email: {self.email}, Org: {User.organization}"
    @classmethod
    def show_total_users(cls):
        """
        Displays total number of users registered.
        """
        print(f"👥 Total users: {cls.total_users}")

 # ------------------------------
# 📌 Demo / App Execution Below
# ------------------------------
if __name__ == "__main__":
    try:
        # Create two users
        user1 = User("Alice", "alice@example.com")
        user2 = User("Bob", "bob@example.com")

        # Show user info
        print(user1.user_info())
        print(user2.user_info())

        # Display total users
        User.show_total_users()

        # Change organization for all users
        User.change_organization("NextGen AI")
    

        # Create a third user with updated organization
        user3 = User("Charlie", "charlie@nextgen.com")
        print(user3.user_info())

        # Display final total
        User.show_total_users()

    except ValueError as e:
        print(e)
