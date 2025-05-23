# Organize code into reusable files (modules) and folders (packages).

# Use import to use code from other modules.# main.py

from animals.dog import Dog
from animals.cat import Cat

d = Dog("Buddy")
c = Cat("Whiskers")

print(d.speak())   # Output: Buddy says Woof!
print(c.speak())   # Output: Whiskers says Meow!
