#Program to Use List Comprehensions

squares = [x**2 for x in range(10)]          # Correctly generating squares of numbers from 0 to 9
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # Correctly generating squares of even numbers from 0 to 9

print("Squares:", squares)           # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("Even squares:", even_squares) # Outputs: [0, 4, 16, 36, 64]

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")