"""
A function is a block of code that performs a specific task. You write it once and use it as many times as you want.

✅ Functions help to organize code, avoid repetition, and make your program cleaner and easier to manage.

"""

# Types of Functions
# Built-in Functions:	Already available in Python (e.g., print(), len(), sum())
# User-defined Functions:	Functions that you create yourself

# 1. 🚀 Simple Function

def greet():
    print("Hello, welcome to Python!")

greet()


print("**********************************")

# 2. 🧾 Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Ali")

print("********************************")

# 3. 🔢 Function with Return Value
def add(a, b):
    return a + b

result = add(5, 6)
print(result)

print("*********************************")

#  📦 Default Parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Sajid")

print("************************************")
# 5. 🎒 Keyword Arguments
def student_info(name, age):
    print(f"Hello, {name}! You are {age} years old.")

student_info(age=18, name="Ali")

print("***************************")

# 6. 🧮 Return Multiple Values
def calaculate(a, b):
    return a + b, a * b, a - b, a / b
sum_, product, difference, quotient = calaculate(10, 5)
print("Sum:", sum_)
print("Product:", product)
print("Difference:", difference)
print("Quotient:", quotient)


print("*********************************")

# 7. 🎯 Function Inside Function

def outer():
    def inner():
        print("This is inner function.")
    print("This is outer function.")
    inner()

outer()


print("************************************")

# 8. ♾️ Recursive Function (Function that calls itself)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))



# 📚 Important Keywords in Functions
# def	To define a function
# return	To return a value from the function
# pass	A placeholder if yo

print("***************************")


# Pass by Reference vs Value
"""
📌 1. Pass by Value (Immutable Types)
When you pass immutable data types like int, float, str, bool, or tuple, Python creates a copy of the value.

Changes inside the function do NOT affect the original value.
"""
def change_value(x):
    x = 10
    print("Inside function:", x)

a = 5
change_value(a)
print("Outside function:", a)  # Still 5
#  int is immutable → so a outside stays unchanged.

print("******************************")

"""
📌 2. Pass by Reference (Mutable Types)
When you pass mutable data types like list, dict, or set, Python passes a reference to the actual object.

Changes inside the function DO affect the original object.
"""

def modify_list(my_list):
    my_list.append(4)
    print("Inside function:", my_list)

nums = [1, 2, 3]
modify_list(nums)
print("Outside function:", nums)  # Changed!


print("*********************")

# # 🌟 Default Arguments in Functions

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Ali")    # Output: Hello, Ali!


def power(base, exponent=2):
    return base ** exponent

print(power(3))       # Output: 9 (3^2)
print(power(2, 3))    # Output: 8 (2^3)


print("*********************************")
# 🌟 Positional-Only Arguments
# Use / to indicate that all arguments before it must be passed by position (not by name)

def divide(a, b, /):
    print(f"Result: {a / b}")

divide(10, 2)     # ✅ Correct usage
# divide(a=10, b=2)  # ❌ Error: a and b must be positional-only


# Another Example

def greet_user(name, /, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Sara")                   # Output: Hello, Sara!
greet_user("Sara", greeting="Hi")    # Output: Hi, Sara!
# greet_user(name="Sara")            # ❌ Error: name must be passed by position


print("*********************************")


# 🌟 Keyword-Only Arguments
# Use * to force arguments after it to be passed by keyword (not position)

def create_user(username, *, role="user"):
    print(f"Username: {username}, Role: {role}")

create_user("Ali", role="admin")   # ✅ Correct usage
# create_user("Ali", "admin")        # ❌ Error: role must be passed as a keyword argument


# Another Example

def print_info(*, name, age):
    print(f"Name: {name}, Age: {age}")

print_info(name="Sara", age=25)  # ✅ All arguments passed as keywords
# print_info("Sara", 25)         # ❌ Error: must use keywords
