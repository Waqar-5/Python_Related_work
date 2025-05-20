# Chapter 05: Control Flow in Python

"""
This chapter covers:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Break and continue statements
- Practical exercises
"""

print("***********************************\n")

# 1. Conditional Statements

age: int = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

print("***********************************\n")

# 2. For Loop

print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()  # new line

print("***********************************\n")

# 3. While Loop

count: int = 5
print("While loop counting down:")
while count > 0:
    print(count, end=" ")
    count -= 1
print()

print("***********************************\n")

# 4. Break Statement
print("Break example:")
for num in range(1, 10):
    if num == 5:
        print("Reached 5, breaking the loop.")
        break
    print(num, end=" ")
print()

print("***********************************\n")

# 5. Continue Statement
print("Continue example (skip even numbers):")
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()

print("***********************************\n")

# 6. Nested Loops

print("Nested loops example (multiplication table 1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # new line after each table

print("***********************************\n")

# 7. Practical Exercises

# EXERCISE 1: Find the largest of three numbers
num1: int = int(input("Enter first number: "))
num2: int = int(input("Enter second number: "))
num3: int = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number is:", largest)

print("***********************************\n")

# EXERCISE 2: Print even numbers between 1 and 20 using a loop
print("Even numbers between 1 and 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

print("***********************************\n")

# EXERCISE 3: Count down from a user input number to zero
start_num: int = int(input("Enter a number to countdown from: "))
while start_num >= 0:
    print(start_num, end=" ")
    start_num -= 1
print()

# Summary
"""
| Control Flow      | Description                                  | Example                   |
|-------------------|----------------------------------------------|---------------------------|
| if, elif, else    | Conditional branching                         | if age > 18: ... else: ...|
| for loop          | Iterate over a sequence or range              | for i in range(5): ...    |
| while loop        | Repeat while condition is True                | while count > 0: ...      |
| break             | Exit loop prematurely                          | if condition: break       |
| continue          | Skip current iteration and continue loop      | if condition: continue    |
| Nested loops      | Loop inside another loop                       | for i in ... for j in ... |
"""
