# 1. Class Decorators
# These are functions that take a class object as an argument and return either the same class or a modified one.

# ✅ Use Case: Logging, registration, permissions, or modification of class attributes/methods.


# Class decorator function
def log_class(cls):
    print(f"[LOG] Creating class: {cls.__name__}")
    return cls

# Apply decorator to the class
@log_class
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

# When the class is defined, the decorator will log the class name
obj = MyClass("Ali")
obj.say_hello()      



print("********************************")


# 2. Property Decorators
# These are used to control access to instance attributes like getter, setter, and deleter methods — but they behave like normal attributes.

# ✅ Use Case: You want to control or validate how values are accessed or set.
# 📌 Example: Using @property, @setter, and @deleter

class Product:
    def __init__(self, price):
        self._price = price    # Private attribute (convention)


    # Getter method
    @property
    def price(self):
        property("Getting the price...")
        return self._price
    
    # setter method
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        print("Setting the price...")
        self._price = value

     # Deleter method
    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Creating object
item = Product(100)

# Access price (call @property)
property(item.price)



# Set new price (calls @price.setter)
item.price = 150

# Try setting a negative price (raises ValueError)
# item.price = -50  # Uncomment to see the error

# Delete the price (calls @price.deleter)
del item.price


print("*********************")

class Circle:
    def __init__(self, radius):
        self._radius = radius  # private attribute

    # Getter method
    @property
    def radius(self):
        return self._radius

    # Setter method with validation
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    # Deleter method
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

circle = Circle(5)
print(circle.radius)  # Calls getter, outputs: 5
circle.radius = 10    # Calls setter
# circle.radius = -1  # Raises ValueError
del circle.radius     # Calls deleter

print("******************************")



# App Idea: Smart Bank Account
# Class decorator to add bank information and welcome message

def bank_info_decorator(cls):
    cls.bank_name = "OpenAI National Bank" # Adding a class attribute
    def welcome_message(self):
        return f"Welcome to {cls.bank_name}, Account Holder: {self.owner}"
    cls.welcome_message = welcome_message
    return cls

@bank_info_decorator
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner  #Account owner name
        self._balance = balance  #Private balance attibute

         # Getter for balance using @property decorator

    @property
    def balance(self):
        print("[INFO] Retrieving the balance...")
        return self._balance
    
    
    # Setter for balance with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        print("[INFO] Setting the new balance...")
        self._balance = amount

         # Method to deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("[ERROR] Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"[SUCCESS] Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")


 # Method to withdraw money with balance check
    def withdraw(self, amount):
        if amount <= 0:
            print("[ERROR] Withdrawal amount must be positive!")
            return
        
        if amount > self.balance:
            print("[ERROR] Insufficient funds for withdraw!")
            return
        self.balance -= amount
        print(f"[SUCCESS] Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")


          # String representation of account info
    def __str__(self):
        return (f"Account Owner: {self.owner}\n"
            f"Bank: {self.bank_name}\n"
            f"Balance: ${self.balance:.2f}")
    
# ---- Main program to demo the BankAccount class ----
if __name__ == "__main__":
    # Create a new bank account with an initial deposit
    account = BankAccount("Ali", 1000)

      # Display welcome message from class decorator
    print(account.welcome_message())
    print(account)  # Show initial account details

    
    print("\n-- Trying deposit and withdrawal operations --")

    account.deposit(500)  # Deposit $500
    account.withdraw(200) # Withdraw $200


  # Attempt invalid operations
    try:
        account.balance = -100  # Invalid balance set (should raise error)
    except ValueError as e:
        print("[EXCEPTION]", e)

    account.withdraw(2000)  # Withdraw more than balance (error)
    account.deposit(-50)    # Deposit negative amount (error)

    print("\nFinal Account Details:")
    print(account)

        