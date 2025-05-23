# Single Responsibility: One reason to change.

# Open/Closed: Open to extension, closed to modification.

# Liskov Substitution: Subtypes replace base types.

# Interface Segregation: Many small interfaces better than one big.

# Dependency Inversion: Depend on abstractions, not concretions.


# Single Responsibility Principle (SRP)
# Bad example: One class does two jobs (user data + data persistence)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print(f"Saving {self.name} to database")

#  Better: Separte classes for separate concerns
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    def save(self, user: User):
        print(f"Saving {user.name} to database")
    
# Usage
user = User("Ali", "ali@example.com")
repo = UserRepository()
repo.save(user)



print("**********************")

"""
2. Open/Closed Principle (OCP)
Definition:
Software entities (classes, functions) should be open for extension, but closed for modification. You should be able to add new functionality without changing existing code.

Why?
Helps avoid bugs by not modifying tested code, and facilitates adding new features easily.

"""
# Example:
# Bad: Modifying class when adding new shapes
class AreaCalculator:
    def calculate_area(self, shape):
        if shape.type == "circle":
            return 3.14 * shape.radius **2
        elif shape.type == "rectangle":
            return shape.width * shape.height
# Good: Use inheritance, extend with new classes instead of modifying existing one
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    
    def area(self):
        return self.width * self.height

# Now, AreaCalculator just calls area on shape, no modification needed to add new shapes
class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()

# Usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
calculator = AreaCalculator()

print(calculator.calculate_area(circle))      # 78.5
print(calculator.calculate_area(rectangle))   # 24


print("****************************")

class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly!")

# Problem: Ostrich violates Liskov Substitution Principle because it can't fly like a Bird

# Solution: Refactor with a base class that fits all derived classes properly

class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    pass

# Now, code that works with FlyingBird can expect fly() to exist,
# and Ostrich doesn't violate LSP since it doesn't pretend to fly.




print("***************************")

"""
4. Interface Segregation Principle (ISP)
Definition:
It's better to have many small, specific interfaces rather than one large, general-purpose interface.

Why?
Clients should only depend on methods they actually use.
"""

# Bad: One big interface with unrelated methods
class Worker:
    def work(self):
        pass
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Working...")
    def eat(self):
        print("Eating...")

class RobotWorker(Worker):
    def work(self):
        print("Working...")
    def eat(self):
        raise NotImplementedError("Robots don't eat")  # Bad

# Good: Separate interfaces for work and eat
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        print("Working...")
    def eat(self):
        print("Eating...")

class RobotWorker(Workable):
    def work(self):
        print("Working...")

# RobotWorker doesn't have to implement eat(), respecting ISP

print("***************************")

"""
5. Dependency Inversion Principle (DIP)
Definition:
Depend on abstractions (interfaces or base classes) rather than on concrete implementations.

Why?
Makes code more flexible, testable, and easier to change implementations.

"""

from abc import ABC, abstractmethod

# Abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

# Concrete implementations
class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} in MySQL database")

class MongoDBDatabase(Database):
    def save(self, data):
        print(f"Saving {data} in MongoDB database")

# High-level module depends on abstraction, not concretion
class UserService:
    def __init__(self, db: Database):
        self.db = db

    def save_user(self, user_data):
        self.db.save(user_data)

# Usage
mysql_db = MySQLDatabase()
service = UserService(mysql_db)
service.save_user("User1")

# Easily switch database without changing UserService
mongo_db = MongoDBDatabase()
service = UserService(mongo_db)
service.save_user("User2")



print("*************************")




# import tkinter as tk
# from abc import ABC, abstractmethod
# from tkinter import messagebox

# # --------------- SOLID: Open/Closed & Dependency Inversion ----------------

# class Shape(ABC):
#     @abstractmethod
#     def area(self) -> float:
#         pass

#     @abstractmethod
#     def __str__(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius

#     def area(self) -> float:
#         return 3.1416 * self.radius ** 2

#     def __str__(self):
#         return f"Circle(radius={self.radius})"

# class Rectangle(Shape):
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

#     def __str__(self):
#         return f"Rectangle(width={self.width}, height={self.height})"

# # --------------- SOLID: Single Responsibility ----------------

# class ShapeRepository:
#     """Manages collection of shapes"""
#     def __init__(self):
#         self.shapes = []

#     def add_shape(self, shape: Shape):
#         self.shapes.append(shape)

#     def remove_shape(self, index: int):
#         if 0 <= index < len(self.shapes):
#             self.shapes.pop(index)

#     def get_all_shapes(self):
#         return self.shapes

# # --------------- SOLID: Interface Segregation ----------------

# class ShapeUI(tk.Frame):
#     """UI to add shapes and display list"""

#     def __init__(self, master, shape_repo: ShapeRepository):
#         super().__init__(master)
#         self.shape_repo = shape_repo
#         self.selected_shape = tk.StringVar(value="Circle")
#         self.create_widgets()

#     def create_widgets(self):
#         # Title
#         title = tk.Label(self, text="SOLID Shapes Manager", font=("Helvetica", 18, "bold"), fg="#2c3e50")
#         title.grid(row=0, column=0, columnspan=3, pady=15)

#         # Shape selector
#         tk.Label(self, text="Select Shape:", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
#         shape_options = ["Circle", "Rectangle"]

#         shape_menu = tk.OptionMenu(self, self.selected_shape, *shape_options, command=self.update_form)
#         shape_menu.grid(row=1, column=1, sticky="ew")

#         # Inputs container
#         self.inputs_frame = tk.Frame(self)
#         self.inputs_frame.grid(row=2, column=0, columnspan=3, pady=10)

#         # Input fields for shape properties
#         self.input_labels = []
#         self.input_entries = []

#         # Add button
#         add_btn = tk.Button(self, text="Add Shape", bg="#27ae60", fg="white", command=self.add_shape)
#         add_btn.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=10)

#         # Shapes Listbox + Scrollbar
#         self.shapes_listbox = tk.Listbox(self, height=8, font=("Courier", 11))
#         self.shapes_listbox.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5)
#         scrollbar = tk.Scrollbar(self, orient="vertical", command=self.shapes_listbox.yview)
#         scrollbar.grid(row=4, column=2, sticky="ns")
#         self.shapes_listbox.config(yscrollcommand=scrollbar.set)

#         # Remove button
#         remove_btn = tk.Button(self, text="Remove Selected", bg="#c0392b", fg="white", command=self.remove_shape)
#         remove_btn.grid(row=5, column=0, columnspan=3, sticky="ew", padx=5, pady=10)

#         # Initialize form inputs
#         self.update_form("Circle")

#     def update_form(self, shape_type):
#         # Clear old inputs
#         for label in self.input_labels:
#             label.destroy()
#         for entry in self.input_entries:
#             entry.destroy()

#         self.input_labels.clear()
#         self.input_entries.clear()

#         # Create inputs based on shape
#         if shape_type == "Circle":
#             lbl = tk.Label(self.inputs_frame, text="Radius:", font=("Arial", 12))
#             lbl.grid(row=0, column=0, sticky="w")
#             ent = tk.Entry(self.inputs_frame)
#             ent.grid(row=0, column=1)
#             self.input_labels.append(lbl)
#             self.input_entries.append(ent)
#         else:
#             lbl1 = tk.Label(self.inputs_frame, text="Width:", font=("Arial", 12))
#             lbl1.grid(row=0, column=0, sticky="w")
#             ent1 = tk.Entry(self.inputs_frame)
#             ent1.grid(row=0, column=1)
#             lbl2 = tk.Label(self.inputs_frame, text="Height:", font=("Arial", 12))
#             lbl2.grid(row=1, column=0, sticky="w")
#             ent2 = tk.Entry(self.inputs_frame)
#             ent2.grid(row=1, column=1)
#             self.input_labels.extend([lbl1, lbl2])
#             self.input_entries.extend([ent1, ent2])

#     def add_shape(self):
#         shape_type = self.selected_shape.get()
#         try:
#             if shape_type == "Circle":
#                 radius = float(self.input_entries[0].get())
#                 if radius <= 0:
#                     raise ValueError("Radius must be positive")
#                 shape = Circle(radius)
#             else:
#                 width = float(self.input_entries[0].get())
#                 height = float(self.input_entries[1].get())
#                 if width <= 0 or height <= 0:
#                     raise ValueError("Width and Height must be positive")
#                 shape = Rectangle(width, height)
#         except ValueError as e:
#             messagebox.showerror("Invalid input", str(e))
#             return

#         self.shape_repo.add_shape(shape)
#         self.refresh_list()
#         self.clear_inputs()

#     def refresh_list(self):
#         self.shapes_listbox.delete(0, tk.END)
#         for idx, shape in enumerate(self.shape_repo.get_all_shapes()):
#             self.shapes_listbox.insert(tk.END, f"{idx+1}. {shape} -> Area: {shape.area():.2f}")

#     def remove_shape(self):
#         selected = self.shapes_listbox.curselection()
#         if not selected:
#             messagebox.showwarning("No selection", "Please select a shape to remove")
#             return
#         idx = selected[0]
#         self.shape_repo.remove_shape(idx)
#         self.refresh_list()

#     def clear_inputs(self):
#         for entry in self.input_entries:
#             entry.delete(0, tk.END)


# # ----------------- Main App Window -----------------

# def main():
#     root = tk.Tk()
#     root.title("SOLID Principles - Shape Manager")
#     root.geometry("400x450")
#     root.configure(bg="#ecf0f1")
#     root.resizable(False, False)

#     shape_repo = ShapeRepository()

#     app = ShapeUI(root, shape_repo)
#     app.pack(fill="both", expand=True, padx=15, pady=15)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

