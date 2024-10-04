#Program to Create and Use a Custom Iterator
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1  # Decrement the index by 1
        return self.data[self.index]

# Create an instance of Reverse
rev = Reverse('giraffe')

# Iterate over the instance and print each character
for char in rev:
    print(char)  # Outputs: e, f, f, a, r, i, g


print("\n This program is written and executed by Harshit Sidher (0221BCA054)")