# Use try-except blocks.

# Create custom exceptions by subclassing Exception.

"""
 Error Handling in OOP (Object-Oriented Programming)
In Python OOP, error handling is crucial for building robust and reliable applications. It allows us to catch and respond to runtime errors gracefully without crashing the entire program.
"""


# Using try-except Blocks in OOP
# You can wrap your object-oriented code inside try-except blocks to handle errors like file not found, division by zero, invalid input, etc.
class Divider:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def divide(self):
        try:
            result = self.numerator / self.denominator
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except TypeError:
            print("Error: Inputs must be numbers.")

# test cases 
d1 = Divider(10, 2)
d1.divide()

d2 = Divider(5, 0)
d2.divide()

d3 = Divider("ten", 5)
d3.divide()



"""
Creating Custom Exceptions in Python
Python lets you define your own exception classes by subclassing the built-in Exception class. This is useful when built-in exceptions aren't descriptive enough for your domain-specific errors.
"""
# syntax 
# class MyCustomError(Exception):
    # pass


print("***********************")

"""
    3. Custom Exceptions in an OOP Project
Let’s use a real-world style example: A banking app where we create custom exceptions for invalid operations.
"""

# Step 1: Define custom exceptions
class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds available balance."""
    pass

class NegativeDepositError(Exception):
    """Raised when a deposit is negative."""
    pass

# Step 2: Create a BankAccount class using OOP
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError("Cannot deposit a negative amount.")
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient balance to withdraw ${amount}.")
        self.balance -= amount
        print(f"{self.owner} withdrew ${amount}. Remaining balance: ${self.balance}")

# Step 3: Handle errors using try-except
try:
    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200)  # Will raise custom error
except NegativeDepositError as nde:
    print(f"Deposit Error: {nde}")
except InsufficientFundsError as ife:
    print(f"Withdrawal Error: {ife}")


print("***********************")
class Divider:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def divide(self):
        try:
            result = self.numerator / self.denominator
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except TypeError:
            print("Error: Inputs must be numbers.")

# Function to safely get numeric input from user
def get_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_input(prompt)

# Main interactive loop
print("🔢 Divider App")
num = get_input("Enter numerator: ")
den = get_input("Enter denominator: ")

divider = Divider(num, den)
divider.divide()




print("*************************")
# divider_app.py

class DivisionError(Exception):
    """Base class for division-related exceptions."""
    pass

class ZeroDenominatorError(DivisionError):
    def __str__(self):
        return "🚫 Cannot divide by zero."

class InvalidInputError(DivisionError):
    def __str__(self):
        return "❌ Inputs must be valid numbers."

class Divider:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def divide(self):
        if not isinstance(self.numerator, (int, float)) or not isinstance(self.denominator, (int, float)):
            raise InvalidInputError()
        if self.denominator == 0:
            raise ZeroDenominatorError()
        return self.numerator / self.denominator

def get_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise InvalidInputError()

def main():
    print("\n🔢 Welcome to the Beautiful Divider App 🔢")
    print("✨ This app safely divides two numbers with style and grace ✨\n")

    try:
        num = get_input("Enter numerator: ")
        den = get_input("Enter denominator: ")
        divider = Divider(num, den)
        result = divider.divide()
        print(f"✅ Result: {result}")
    except DivisionError as e:
        print(f"{e}")

if __name__ == "__main__":
    main()



print("***************************")
# smart_divider_app.py
# A Real-Life, Beautiful Divider App with Enhanced Features and Error Handling

class DivisionError(Exception):
    """Base class for division-related exceptions."""
    pass

class ZeroDenominatorError(DivisionError):
    def __str__(self):
        return "🚫 Error: You cannot divide by zero."

class InvalidInputError(DivisionError):
    def __str__(self):
        return "❌ Error: Please enter valid numeric inputs."

class Divider:
    def __init__(self):
        self.history = []  # Store past operations for reference

    def divide(self, numerator, denominator):
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise InvalidInputError()
        if denominator == 0:
            raise ZeroDenominatorError()
        result = numerator / denominator
        self.history.append((numerator, denominator, result))
        return result

    def show_history(self):
        if not self.history:
            print("🕑 No calculations yet.")
        else:
            print("\n📜 Calculation History:")
            for i, (num, den, res) in enumerate(self.history, 1):
                print(f" {i}. {num} ÷ {den} = {res}")

def get_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise InvalidInputError()

def display_welcome():
    print("""
╔══════════════════════════════════════╗
║     🧮  SMART DIVIDER APP v2.0       ║
╠══════════════════════════════════════╣
║  Divide safely with elegance, style ║
║  and history tracking!              ║
╚══════════════════════════════════════╝
    """)

def main():
    divider = Divider()
    display_welcome()

    while True:
        try:
            num = get_input("Enter numerator: ")
            den = get_input("Enter denominator: ")
            result = divider.divide(num, den)
            print(f"✅ Result: {num} ÷ {den} = {result:.2f}")
        except DivisionError as e:
            print(f"{e}")

        print("\nOptions:")
        print(" 1. Try another division")
        print(" 2. View history")
        print(" 3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "2":
            divider.show_history()
        elif choice == "3":
            print("👋 Thanks for using the Smart Divider App. Goodbye!")
            break

if __name__ == "__main__":
    main()


