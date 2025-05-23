# Method Resolution Order (MRO)

# to Check MRO?
# ClassName.__mro__
# or 
# ClassName.mro()

# Single Inheritance

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

b = B()
b.greet()  # Output: Hello from A

# Check MRO
print(B.mro())  
# Output: [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]



print("****************************")

# Multiple Inheritance Example
class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):
# class D(C, B):
    pass

d = D()
# d = C()
d.show()  # Output: B.show()

# Check MRO
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


print("****************************")

#  Diamond Problem Example

class A:
    def whoami(self):
        print("I am A")

class B(A):
    def whoami(self):
        print("I am B")

class C(A):
    def whoami(self):
        print("I am C")

class D(B, C):  # D -> B -> C -> A
    pass

d = D()
d.whoami()  # Output: I am B

# Check MRO
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

print("***************************")
#  Custom Example with super() and MRO
class A:
    def do(self):
        print("A.do")

class B(A):
    def do(self):
        print("B.do")
        super().do()

class C(A):
    def do(self):
        print("C.do")
        super().do()

class D(B, C):  # MRO: D -> B -> C -> A
    def do(self):
        print("D.do")
        super().do()

d = D()
d.do()

# Output:
# D.do
# B.do
# C.do
# A.do

# Check MRO
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]



# 🎨 Shape Drawer App
from termcolor import colored

# 🧱 Base class for all shapes
class Shape:
    def draw(self):
        # This will be called last in MRO chain
        print(colored("Drawing base Shape...", "white"))

# 🔵 Circle inherits from Shape
class Circle(Shape):
    def draw(self):
        print(colored("Drawing a Circle 🟢", "green"))
        # Call the next class in MRO chain
        super().draw()

# 🟥 Rectangle inherits from Shape
class Rectangle(Shape):
    def draw(self):
        print(colored("Drawing a Rectangle 🟥", "red"))  
        # call the next class in MRO chain
        super().draw()


# 🔺 Triangle inherits from Shape
class Triangle(Shape):
    def draw(self):
        print(colored("Drawing a Triangle 🔺", "yellow"))
        # Call the next class in MRO chain
        super().draw()

# 🧩 Final class combining multiple shapes
class ArtPiece(Circle, Rectangle, Triangle):
    def draw(self):
        print(colored("Starting ArtPiece Drawing 🎨", "cyan", attrs=["bold"]))
        # This super() will start the MRO chain: Circle -> Rectangle -> Triangle -> Shape
        super().draw()
        print(colored("Finished ArtPiece 🎉", "cyan", attrs=["bold"]))


# 👨‍🎨 Create an instance of ArtPiece and draw it
art = ArtPiece()
art.draw()

# 📜 Print the MRO to show method resolution order
print(colored("\nMethod Resolution Order (MRO):", "blue", attrs=["bold"]))
for cls in ArtPiece.mro():
    print(colored(f"- {cls.__name__}", "magenta"))


print("****************************")
# Vehicle Control System

from termcolor import colored

# 🚘 Base Vehicle class
class Vehicle:
    def start(self):
        print(colored("🔑 Starting vehicle system...", "white"))

# ⚡ Electric system (inherits from Vehicle)
class Electric(Vehicle):
    def start(self):
        print(colored("🔋 Activating electric battery system...", "green"))
        super().start()  # Call next class in MRO

# 🤖 Autonomous system (inherits from Vehicle)
class Autonomous(Vehicle):
    def start(self):
        print(colored("🧠 Initializing autonomous driving AI...", "yellow"))
        super().start()  # Call next class in MRO

# 🏎 Real-life car with both Electric and Autonomous systems
class TeslaModelX(Electric, Autonomous):
    def start(self):
        print(colored("🚗 Tesla Model X Boot Sequence 🔽", "cyan", attrs=["bold"]))
        super().start()  # Start the full boot chain
        print(colored("✅ Tesla Model X is ready to drive!", "cyan", attrs=["bold"]))

# 🧪 Create a Tesla car and start it
car = TeslaModelX()
car.start()

# 🧾 Show method resolution order
print(colored("\nMethod Resolution Order (MRO):", "blue", attrs=["bold"]))
for cls in TeslaModelX.mro():
    print(colored(f"- {cls.__name__}", "magenta"))
