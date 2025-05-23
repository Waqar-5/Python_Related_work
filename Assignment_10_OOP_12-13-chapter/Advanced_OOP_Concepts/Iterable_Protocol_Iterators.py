# Define __iter__() returning iterator and __next__() for iteration.

# Use in for loops.
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # __iter__ must return an iterator object
        # Here we return an instance of MyRangeIterator
        # which will handle the actual iteration logic
        return MyRangeIterator(self.start, self.end)


class MyRangeIterator:
    def __init__(self, start, end):
        # Initialize current position for iteration
        self.current = start
        self.end = end

    def __iter__(self):
        # Iterator's __iter__ should return self
        # This allows the iterator itself to be used as an iterable
        return self

    def __next__(self):
        # __next__ returns the next item in the sequence
        # If no more items, raise StopIteration to signal the end
        if self.current >= self.end:
            raise StopIteration  # Signals that iteration is complete
        else:
            # Return current value and move forward
            val = self.current
            self.current += 1
            return val


# Using the iterable in a for loop
my_range = MyRange(1, 5)

for num in my_range:
    print(num)


print("*************************")
# App Idea: Countdown Timer with Custom Iterable
import time

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Return the iterator object that does the countdown
        return CountdownIterator(self.start)

class CountdownIterator:
    def __init__(self, count):
        self.current = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            # Stop iteration once countdown is finished
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val

def run_countdown(start):
    print(f"Starting countdown from {start}...\n")
    for number in Countdown(start):
        print(number)
        time.sleep(1)  # Wait for 1 second to simulate timer
    print("\nCountdown complete!")

# Run the countdown app
if __name__ == "__main__":
    run_countdown(5)


"""
Why this is a wonderful example:
It’s practical — you get a visible countdown.

It shows how __iter__() and __next__() work together to produce a sequence.

Uses StopIteration to cleanly end the sequence.

Includes a real-world effect (timer with delay).

Easy to customize — just change the starting number.


"""

