# __call__ in Action
# Define a class called Multiplier
class Multiplier:
    # Constructor (__init__) to set the factor during object creation
    def __init__(self, factor):
        self.factor = factor  # Store the factor as an instance variable

    # Define the __call__ method to make the object callable
    def __call__(self, value):
        return value * self.factor  # Multiply the given value by the stored factor

# Using the Multiplier class

# Create an instance of Multiplier with a factor of 3
triple = Multiplier(3)

# Check if the object 'triple' is callable using callable()
print(callable(triple))  # Output: True

# Now call the instance like a function
print(triple(10))  # Output: 30 → Equivalent to 10 * 3




print("**************************")


# Explanation with Line-by-Line Comments
# Define a class named Multiplier
class Multiplier:

    # The __init__ method initializes the object with a factor
    def __init__(self, factor):
        self.factor = factor  # Save the factor to use later in __call__

    # The __call__ method is what makes an instance behave like a function
    def __call__(self, value):
        return value * self.factor  # Perform multiplication using the stored factor

# Create an instance with a factor of 3
triple = Multiplier(3)

# Check if the object is callable (has a __call__ method)
print(callable(triple))  # Output: True

# Call the object like a function; it runs the __call__ method
print(triple(10))  # Output: 30 (3 * 10)

print("***********************")
# ✅ Real-World Example: Logger# A simple Logger class that logs messages when called
class Logger:
    def __init__(self, prefix):
        self.prefix = prefix  # Prefix to identify the source of the log

    def __call__(self, message):
        print(f"{self.prefix}: {message}")  # Format and print the message
# Create a logger for "INFO" messages
info_logger = Logger("INFO")

# Call the logger object like a function
info_logger("System started")  # Output: INFO: System started



print("**************************")
# temperature_converter.py
# Define a class to convert temperature from Celsius to Fahrenheit or Kelvin

class TemperatureConverter:
    def __init__(self, target_unit):
          """
        Initialize with the target unit.
        Acceptable values: 'fahrenheit' or 'kelvin'
        """
          self.target_unit = target_unit.lower()  # Convert to lowercase for consistency

    def __call__(self, celsius_temp):
         """
        Make the instance callable to convert temperature from Celsius to the target unit.
        """
         if self.target_unit == "fahrenheit":
             return (celsius_temp * 9/5) + 32  # Celsius to Fahrenheit formula
         
         elif self.target_unit == "kelvin":
             return celsius_temp + 273.15  # Celsius to Kelvin formula 
         else:
             raise ValueError(f"Unsupported unit: {self.target_unit}. Choose 'fahrenheit' or 'kelvin'.")
         
    def __str__(self):
                """
                Provide a user-friendly string representation.
                """
                return f"TemperatureConverter to {self.target_unit.capitalize()}"


             

# ===============================
# Example Usage
# ===============================

#  Create a converter instance to convert to Fahrenheit
to_fahrenheit = TemperatureConverter("fahrenheit")


   # Create another converter instance to convert to Kelvin
to_kelvin = TemperatureConverter("kelvin")       


# Print string representations
print(to_fahrenheit)  # Output: TemperatureConverter to Fahrenheit
print(to_kelvin)      # Output: TemperatureConverter to Kelvin

# Convert some temperatures
print("25°C in Fahrenheit:", to_fahrenheit(25))  # Output: 77.0
print("0°C in Kelvin:", to_kelvin(0)) 

# Check if the objects are callable
print("Is to_fahrenheit callable?", callable(to_fahrenheit))  # Output: True
print("Is to_kelvin callable?", callable(to_kelvin))          # Output: True

# Trying an invalid unit will raise an error
try:
    to_unknown = TemperatureConverter("rankine")
    print(to_unknown(100))
except ValueError as e:
    print("Error:", e)
    
    
    """
    ✨ Features Demonstrated
__init__: Initialize with a target conversion unit.

__call__: Make the object behave like a function.

__str__: Provide a clean string for print().

callable(): Check if an object supports calling.

try...except: Gracefully handle invalid input.


    """

print("**********************************")


# 🌟 App Idea: Personal Greeter Bot (Callable Class)

# Define the GreeterBot class
class GreeterBot:
    def __init__(self, mood):
           """
        Initialize the bot with a specific mood.
        Moods can be: 'happy', 'sad', 'energetic'
        """
           self.mood = mood.lower()

    def __call__(self, name):
          """
        Call the bot like a function with the person's name.
        The greeting changes based on the bot's mood.
        """
          if self.mood == "Happy":
                return f"🤖 HappyBot: Hello, {name}! 😊"
          elif self.mood == "sad":
                return f"🤖 SadBot: Oh... hi, {name}. 😔"
          elif self.mood == "energetic":
               return f"🤖 EnergeticBot: Heyyy {name}!!! 🔥🔥🔥"
          else:
               return f"🤖 NeutralBot: Hi {name}."
         

    def __str__(self):
        """
        Pretty print the mood of the bot.
        """
        return f"GreeterBot in '{self.mood}' mood"

          
# ===============================
# 🎉 App Demo
# ===============================


# Create bots with different moods
happy_bot = GreeterBot("happy")
sad_bot = GreeterBot("sad")
energetic_bot = GreeterBot("energetic")
unknown_bot = GreeterBot("curious")  # Undefined mood

# Print bot identities
print(happy_bot)       # GreeterBot in 'happy' mood
print(sad_bot)         # GreeterBot in 'sad' mood
print(energetic_bot)   # GreeterBot in 'energetic' mood
print(unknown_bot)     # GreeterBot in 'curious' mood

# Use bots like functions
print(happy_bot("Asad"))         # 🤖 HappyBot: Hello, Alice! 😊
print(sad_bot("Ameer"))             # 🤖 SadBot: Oh... hi, Bob. 😔
print(energetic_bot("Sameer"))   # 🤖 EnergeticBot: Heyyy Charlie!!! 🔥🔥🔥
print(unknown_bot("Khan"))        # 🤖 NeutralBot: Hi Dana.

# Check if bots are callable
print(callable(happy_bot))        # True
print(callable(sad_bot))          # True



"""
# ===============================
# 🖥️ User Interaction
# ===============================

# Ask the user for the mood of the bot
user_mood = input("Enter the mood of your bot (happy, sad, energetic): ")

# Create a bot with that mood
bot = GreeterBot(user_mood)

# Display the bot's current mood
print(f"\nBot created: {bot}")
print("Type 'exit' to quit.\n")

# Loop to greet multiple people
while True:
    name = input("Enter a name to greet: ")

    if name.lower() == 'exit':
        print("👋 Goodbye!")
        break

    # Use the bot like a function
    print(bot(name))
"""