#Program to Use a Generator with a Loop
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for num in fibonacci(10):  # Correctly call the generator function
    print(num)  # Outputs: 0, 1, 1, 2, 3, 5, 8


print("\n This program is written and executed by Harshit Sidher (0221BCA054)")