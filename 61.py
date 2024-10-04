#Program to Use Generator with yield
def countdown(n):
    while n > 0:  # Add a colon at the end of the while statement
        yield n
        n -= 1  # Use `-= 1` to decrement n correctly

for number in countdown(5):  # Add a closing parenthesis
    print(number)  # Outputs: 5, 4, 3, 2, 1

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")