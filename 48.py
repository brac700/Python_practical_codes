def is_prime(n):
    """Check if the number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if the number is perfect."""
    if n < 2:
        return False
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

def is_armstrong(n):
    """Check if the number is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return sum_of_powers == n

def find_numbers(limit):
    print(f"Numbers smaller than {limit}:")
    
    print("\nPrime Numbers:")
    for num in range(2, limit):
        if is_prime(num):
            print(num, end=' ')

    print("\n\nPerfect Numbers:")
    for num in range(1, limit):
        if is_perfect(num):
            print(num, end=' ')

    print("\n\nArmstrong Numbers:")
    for num in range(limit):
        if is_armstrong(num):
            print(num, end=' ')

# Get user input
try:
    user_input = int(input("Enter a positive integer: "))
    find_numbers(user_input)
except ValueError:
    print("Please enter a valid integer.")


print("\n This program is written and executed by Harshit Sidher (0221BCA054)")