def precompute_powers(max_digits):
    # Precompute and store powers from 0^1 to 9^max_digits
    powers = [[(digit ** exp) for exp in range(max_digits + 1)] for digit in range(10)]
    return powers

def is_armstrong(number, powers):
    # Convert number to string to easily iterate digits
    digits = list(map(int, str(number)))
    num_digits = len(digits)
    
    # Sum the power of digits
    armstrong_sum = sum(powers[digit][num_digits] for digit in digits)
    return armstrong_sum == number

def print_armstrong_numbers(limit):
    # Determine the maximum number of digits to check based on limit
    max_digits = len(str(limit))
    
    # Precompute all powers from 0^1 to 9^max_digits
    powers = precompute_powers(max_digits)
    
    # Check all numbers from 1 up to limit for Armstrong property
    for num in range(1, limit + 1):
        if is_armstrong(num, powers):
            print(num)

# Example usage: print Armstrong numbers up to 10000
print_armstrong_numbers(100000000000000000000000000000000000000000000000000000000)