"""
 How to Import a Module in Python
In Python, importing a module means bringing in some code (functions, variables, classes) so you can use it in your program.
"""

# 1. ✅ Import the Entire Module
import math

print(math.sqrt(16))  # Output: 4.0
# 🟢 You must use the module name (math) before using its functions.

print("***********************")


# 2. ✅ Import Specific Functions or Variables

from math import sqrt, pi

print(sqrt(25))
print(pi)  # Output: 3.14159...
# 🟢 You don’t need to use the module name, only the function name.

print("************************")


# ⚠️ Import Everything (Not Recommended)
from math import *

print(sqrt(36))   # Output: 6.0
print(factorial(5))  # Output: 120
# ⚠️ This imports all functions, which can cause name conflicts in big programs.

print("*************************")
# 4. ✍️ Import with an Alias (Nickname)
import math as m 
print(m.sqrt(49))  # Output: 7.0


"""
import module	Imports full module
from module import x	Imports specific part of the module
from module import *	Imports everything (not recommended)
import module as nickname	Imports with a shortcut name (alias)

"""
