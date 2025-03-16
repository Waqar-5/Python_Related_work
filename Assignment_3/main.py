# Control Flow and Decision Making in Python
# Conditional Statements (if, elif, else)
# Conditional statements control the flow of a program based on conditions.

# examples
age = 18

if age >= 18:
    print("You are eligible to vote.")
elif age > 16:
    print("You will be eligible to voyte soon.")
else:
    print("You are not eligible to vote yet.")

"""🔹 Explanation:

The if statement checks the first condition.
The elif statement provides an alternative check.
The else block executes if none of the conditions are met"""



num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")



print("**************************")

# Loops in Python
# Loops are used to repeat a block of code multiple times.
# for loop 
# A for loop is used when you want to iterate over a sequence (like a list, tuple, or range).

for i in range(5):
    print("Ïteration:", i )
"""
The range(5) generates numbers from 0 to 4.
The loop prints the value of i in each iteration.

"""

num = int(input("Ënter a number:" ))
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")




print("***************************")
#  While Loop
# A while loop runs as long as the condition is True.

count = 0
while count < 5:
    print("Count:", count)
    count += 1

    """The loop starts with count = 0 and runs until count reaches 5.
count += 1 increases the value in each iteration to avoid an infinite loop.
"""

print("***********************************")

import random

secret_number = random.randint(1,10)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10:"))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulation! You guessed the right number 💐")

# While Loop with else: Checking Prime Numbers
num = int(input("Enter a number: "))

if num > 1:
    for i in range(1, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{num} is a prime number")
    else:
        print("Enter a number greater than 1.")


print("*******************************")
# Nested Loops
# Loops inside loops are called nested loops.
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j={j}")

"""
The outer loops runs 3 times (i = 0, 1,2)
The inner loops runs 2 times for each iteraion of the outer loop
"""

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()



# Loop Control: Skipping Even Numbers with continue
for num in range(1, 11):
    if num % 2 == 0:
        continue # skips even number
    print("odd number :",num)

    # Using break: Stopping the Loop at a Certain Condition
    for i in range(1, 10):
        if i == 5:
            print("Loop stopped at", i)
            break
        print(i)


print("***********************************")

# 4. Loop Control Statements
# break - Exits the loop.
# continue - Skips the current iteration.
# pass - Does nothing (used as a placeholder).

for num in range(10):
    if num == 5:
        break # stops the loop when num is 5
    if num == 3:
        continue # skips when num is 3
    print(num)

# break stops the loop when num == 5.
# continue skips printing 3 and moves to the next iteration.
