
# What is the object Class?
# In Python, everything is an object. Every class you create automatically inherits from a built-in base class called object.

# ✅ Why is object important?
# It is the root/base class of all other classes in Python.

# It provides some common default methods to all objects:

# __str__() → returns a user-friendly string representation of the object.

# __repr__() → returns a developer-friendly string representation.

# __eq__() → for comparing two objects.

# __init__() → constructor method (not from object, but commonly overridden).


#  Basic Inheritance from object
# A simple class that does not explicitly inherit from anything
class Animal:
    pass

# Let's check its base class
print(Animal.__bases__)  # Output: (<class 'object'>,)


print("********************************")


#  2: Using __str__() and __repr__() from object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # User-friendly string (used when you print the object)
    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"
    
     # Developer-friendly string (used in debugging)

    def __repr__(self):
        return f"Person(name='{self.name}', age{self.age})"
    


# create object  
p = Person("Ali", 30)


# __str__ is sued by print()
print(p) #Output: Person: Ali, 30 years old

# __repr__ is sued in debugging
print(repr(p)) # Output: Person(name='Ali', age=30)



print("**************************")

# 3: How object helps with comparison using __eq__()
class Car:
    def __init__(self, model):
        self.model = model
    
    def __eq__(self, other):
        return self.model == other.model
    

car1 = Car("Tesla")
car2 = Car("Tesla")
car3 = Car("Toyota")

print(car1 == car2)  # True, because models are equal
print(car1 == car3)  # False

print("************************")

# contact_book.py

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

          # User-friendly string (used when printing the object)
    def __str__(self):
        return f"{self.name} 📞 {self.phone} ✉️ {self.email} "
    

     # Developer-friendly string (used in logs/debugging)
    def __repr__(self):
        return f"Contact(name='{self.name}', phone='{self.phone}', email='{self.email}')"
    

    # Custom equality: Two contacts are equal if their phone numbers match
    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        return self.phone == other.phone
    

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add__contact(self, contact):
        if contact in self.contacts:
              print(f"⚠️ Contact with phone {contact.phone} already exists!")
        else:
            self.contacts.append(contact)
            print(f"✅ Contact {contact.name} added successfully!")

    def show_contacts(self):
        print("\n📖 Contact List:")
        for c in self.contacts:
               print(f"• {c}")  # Uses __str__ of Contact


    def debug_print(self):
        print("\n🐞 Raw Contact Objects (for developers):")
        print(self.contacts)  # Uses __repr__ of each Contact




# ------------------- Main Program -------------------

if __name__ == "__main__":
      print("🔹 Welcome to Contact Book App 🔹")

      book = ContactBook()

    #   Creating contacts
      c1 = Contact("Aisha", "123-456-7890", "aisha@example.com")
      c2 = Contact("Ahmed", "987-654-3210", "ahmed@example.com")
      c3 = Contact("Aisha", "123-456-7890", "aisha.duplicate@example.com")  # Same phone!

    # Adding contacts
      book.add__contact(c1)
      book.add__contact(c2)
      book.add__contact(c3)  # Should show duplicate warning due to same phone

    # Displaying contacts
      book.show_contacts()

    # Debugging output
      book.debug_print()

    #   or 
    
# ------------------- Main Program with User Input -------------------

# def main():
#     print("🔹 Welcome to Contact Book App 🔹")
#     book = ContactBook()

#     while True:
#         print("\nWhat would you like to do?")
#         print("1. Add a new contact")
#         print("2. Show all contacts")
#         print("3. Debug (show raw objects)")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ").strip()

#         if choice == '1':
#             name = input("Enter name: ").strip()
#             phone = input("Enter phone number: ").strip()
#             email = input("Enter email: ").strip()
#             contact = Contact(name, phone, email)
#             book.add__contact(contact)

#         elif choice == '2':
#             book.show_contacts()

#         elif choice == '3':
#             book.debug_print()

#         elif choice == '4':
#             print("👋 Exiting... Goodbye!")
#             break

#         else:
#             print("❌ Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()