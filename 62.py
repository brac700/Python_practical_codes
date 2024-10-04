#Program to Use yield in a Custom Iterator
class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        while self.n > 0:  # Add a colon here
            yield self.n
            self.n -= 1  # Correctly decrement self.n

# Create an instance of Countdown and iterate over it
for number in Countdown(5):  # Add closing parenthesis
    print(number)  # Outputs: 5, 4, 3, 2, 1

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")