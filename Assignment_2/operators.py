# operators
# Operators in programming are special symbols that perform operations on operands. In Python (or other languages like JavaScript, TypeScript), we have several types of operators. Let’s go through each type one by one with examples.

# 1. Arithmetic operators

# These operators perform mathematical operations like addition, subtraction, multiplication, and division.

# (Addition operator) = +
# (Substraction operator) = -
# (Multiplication operator) = *
# (Division(float) operator) = /
# (floor operator) = //
# (modulus(remainder) operator) = %
# (Exponentiation operator) = **

# examples
a = 10
b = 3
print("Arithmetic operators")
print("Addition:", a + b)  #13
print("Substraction:", a-+ b) # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b) # 3.33
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)  # 1
print("Exponentiation:", a ** b)  # 1000

print("*******************************")


# 2. comparsion(Relational) operators
# These operators compare two values and return a Boolean result (True or False).
""""
== (equal to )
!= (not equal to) 
> (greater than)
< (less than)
>= (greater than or equal to)
<= (less than or equal to) 
"""

# examples
x = 10
y = 5
print("Comparsion Operators")
print(x == y) # false
print(x != y) # true
print(x > y) # true
print(x < y) # false
print(x >= y) # true
print(x <= y) # false


print("****************************")
# 3. Logical Operators
# Logical operators are used to combine multiple conditions.
"""
and (Returns True if both conditions are true)
or (returns True if at least one condition is true)
not (reverse the Boolean value)
"""

# examples
c = 10
d = 5
e = 2
print("Logical operators")
print((c > d) and (d > e)) # True (both conditions are ture)
print((c > d) or (d < e)) # True (one conditions is ture)
print(not (c > d)) # True (negates True to False)


print("****************************")

# 4. Bitwise Operators
# These operators work at the bit level.

"""
& (bitwise AND)
` (bitwise or)
^  (bitwise XOR)
~ (Bitwise NOT)
<< (Left Shift)
>> (Right Shift)
"""

# Example in Python
f = 5 # 0101 in binary
g = 3 # 0011 in binary
print("Bitwise operators")
print("Bitwise AND:", f & g) # 1
print("Bitwise OR:", f | g) # 7
print("Bitwise XOR:", f ^ g) # 6
print("Bitwise NOT:", ~f) # -6
print("Left Shift:", f << 1) # 10(1010 in binary)
print("Right Shift:", f >> 1) # 2 (0010 in binary)

print("************************")


# 5. Assignment Operators
# These are used to assign values to variables.

"""
=
+= ( Add and Assign )
-= (Subtract and Assign)
*= (Multiply and Assign)
/= (Divide and Assign)
//= (Floor Divide and Assign)
%= (Modulus and Assign)
**= (Exponentiate and Assign)
"""
print("Assignment operators")
h = 10
print(h)
hi = 10
hi += 5
print(hi) # 15
h1 = 10 
h1 -= 3
print(h1) # 7
h2 = 4
h2 *= 3
print(h2)
h3 = 10
h3 /= 2
print(h3) # 5.0
h4 = 10
h4 //= 3
print(h4) # 3
h5 = 10
h5 %= 3
print(h5) # 1
h6 = 2
h6 **= 3
print(h6) # 8




print("**************************")


# 6. Identity Operators
# These check whether two variables point to the same memory location.

"""
is (returns True if both variables refer to the same object)
is not (Returns True if both variables do not refer to the same object)

"""

# examples
num = [1, 2, 3,]
num1 = num
num2 = [1, 2, 3]
print("identity Operators")
print(num is num1) # True (same object)
print(num is num2) # False (different objects)
print(num is not num2) # True


print("****************************")
# 7. Membership Operators
# These are used to check whether a value exists in a sequence (list, tuple, string, etc.).

"""
in (returns True if value is found in the sequence)
not in (returns True if value is not found in the sequence)
"""
# Example

fruits = ["apple", "banana", "cherry"]
print("Membership Operators")
print("banana" in fruits) # true
print("grape" not in fruits) # true

