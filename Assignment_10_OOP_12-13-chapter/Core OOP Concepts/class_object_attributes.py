# Define a class named 'Book' - a blueprint for book objects
class Book:
      # Constructor method to initialize each book object with title and author
      def __init__(self, title, author):
          self.title = title # Instance attribute unique to each book
          self.author = author # Instance attribute unique to each book

        # Instance method to display book details
      def display_info(self):
           print(f"'{self.title}' by {self.author}")


        
# The class 'Book' itself is NOT an object, it's a blueprint/template.

# Create (instantiate) objects of the Book class
book1 =  Book("1984", "George Orwell")      # book1 is an instance (object) of Book
book2 = Book("To Kill a Mockingbird", "Harper Lee")  # book2 is another instance (object)


# Access instance methods through objects
book1.display_info()   # Output: '1984' by George Orwell
book2.display_info()     # Output: 'To Kill a Mockingbird' by Harper Lee


# Show that book1 and book2 are distinct objects (instances) of the Book class
print(f"Type of book1: {type(book1)}")  # <class '__main__.Book'>
print(f"Type of book2: {type(book2)}")  # <class '__main__.Book'>


print(f"Is book1 an instance of Book? {isinstance(book1, Book)}")  # True
print(f"Is book2 an instance of Book? {isinstance(book2, Book)}")  # True

# The 'Book' class itself can be accessed and is of type 'type'
print(f"Type of Book class: {type(Book)}")  # <class 'type'>  



print("***********************")

# Define a class 'Computer' as a blueprint for creating computer objects
class Computer:
    # Class attribute: shared by all Computer objects
    manufacturer = "TechCorp"

    # Constructor to initialize instance attributes for each object
    def __init__(self, model, ram_gb):
        self.model = model      # Instance attribute unique to each computer
        self.ram_gb = ram_gb    # Instance attribute unique to each computer

    # Instance method to display computer details
    def display_specs(self):
        print(f"Manufacturer: {Computer.manufacturer}")  # Access class attribute via class name
        print(f"Model: {self.model}")                     # Instance attribute
        print(f"RAM: {self.ram_gb} GB")                   # Instance attribute

# The 'Computer' class itself is a blueprint, not an object

# Create two objects (instances) of Computer class
comp1 = Computer("X1000", 16)  # comp1 is an instance/object of Computer
comp2 = Computer("Z2000", 32)  # comp2 is another instance/object of Computer

# Access class attribute via objects and class
print(f"Access via class: {Computer.manufacturer}")  # TechCorp
print(f"Access via object: {comp1.manufacturer}")    # TechCorp

# Show that comp1 and comp2 have their own instance attributes
comp1.display_specs()
# Output:
# Manufacturer: TechCorp
# Model: X1000
# RAM: 16 GB

comp2.display_specs()
# Output:
# Manufacturer: TechCorp
# Model: Z2000
# RAM: 32 GB

# Demonstrate that comp1 and comp2 are distinct objects (instances)
print(f"comp1 is instance of Computer: {isinstance(comp1, Computer)}")  # True
print(f"comp2 is instance of Computer: {isinstance(comp2, Computer)}")  # True

# Changing class attribute affects all instances
Computer.manufacturer = "NewTech"

print("\nAfter changing class attribute:")
comp1.display_specs()
comp2.display_specs()

# Creating an instance attribute with same name hides the class attribute for that object only
comp1.manufacturer = "CustomTech"

print("\nAfter adding instance attribute to comp1:")
print(f"comp1.manufacturer (instance attribute): {comp1.manufacturer}")  # CustomTech
print(f"comp2.manufacturer (class attribute): {comp2.manufacturer}")    # NewTech
print(f"Computer.manufacturer: {Computer.manufacturer}")                 # NewTech
