class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner # Public attribute
        self._balance = balance     # Protected attribute (suggests internal use)
        self.__pin = pin            # Private attribute (name-mangled)

 # Public method to show balance (acts like a getter)
    def show_balance(self, input_pin):
        if input_pin == self.__pin:
            print(f"{self.owner}'s balance: ${self._balance}")
        else:
            print("Access denied: Incorrect PIN")

            
    # Public method to deposit money (acts like a setter)
    def deposit(self, amount, input_pin):
        if input_pin == self.__pin:
            self._balance += amount
            print(f"Deposited ${amount}. New Balance: ${self._balance}")
        else:
            print("Access Denied: Incorrect PIN")

        #Public method to change PIN (setter)
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN!")

        
# Create an account object
account = BankAccount("Ali", 5000, 1234)


# Accessing public attribute
print(f"Account owner: {account.owner}")

# Accessing protected attribute (allowed, but not recommended)
print(f"Accessing protected balance directly: ${account._balance}")

# Accessing private attribute directly will cause an error
# print(account.__pin)  # ❌ Will raise AttributeError

# But can still be accessed using name mangling (not recommended)
print(f"Accessing private pin (not recommended): {account._BankAccount__pin}")



# Using public methods (getters/setters)
print("\n--- Using methods with PIN ---")
account.show_balance(1234)
account.deposit(1000, 1234)
account.change_pin(1234, 5678)
account.show_balance(5678)


print("*******************************")

class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # Public attribute
        self._balance = balance     # Protected attribute
        self.__pin = pin            # Private attribute (name mangling for security)

    # Method to show balance (requires PIN)
    def show_balance(self, input_pin):
        if input_pin == self.__pin:
            print(f"\n✅ {self.owner}'s Current Balance: ${self._balance}")
        else:
            print("❌ Incorrect PIN! Access Denied.")

    # Method to deposit money (requires PIN)
    def deposit(self, amount, input_pin):
        if input_pin == self.__pin:
            self._balance += amount
            print(f"✅ ${amount} deposited. New Balance: ${self._balance}")
        else:
            print("❌ Incorrect PIN! Cannot deposit.")

    # Method to change PIN securely
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("🔐 PIN changed successfully!")
        else:
            print("❌ Old PIN is incorrect. Cannot change PIN.")

# 📌 Step 1: Create a new bank account with user input
owner = input("Enter your name: ")
balance = float(input("Enter initial balance: "))
pin = int(input("Set your 4-digit PIN: "))

# Create an object (account) with the user's data
account = BankAccount(owner, balance, pin)

while True:
    print("\n💼 BANK MENU")
    print("1. Show Balance")
    print("2. Deposit Money")
    print("3. Change PIN")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        entered_pin = int(input("Enter PIN to view balance: "))
        account.show_balance(entered_pin)

    elif choice == "2":
        entered_pin = int(input("Enter PIN to deposit: "))
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount, entered_pin)

    elif choice == "3":
        old_pin = int(input("Enter current PIN: "))
        new_pin = int(input("Enter new 4-digit PIN: "))
        account.change_pin(old_pin, new_pin)

    elif choice == "4":
        print("👋 Thank you for using the bank system!")
        break

    else:
        print("❗ Invalid choice! Please select from 1 to 4.")
