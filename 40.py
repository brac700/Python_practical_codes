def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_cubes_of_primes(lower_limit, upper_limit):
    total_sum = 0
    for num in range(lower_limit, upper_limit + 1):
        if is_prime(num):
            total_sum += num ** 3
            print(f"Prime number: {num}, Cube: {num ** 3}")
    return total_sum


lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

result = sum_of_cubes_of_primes(lower_limit, upper_limit)
print("The sum of cubes of prime numbers between", lower_limit, "and", upper_limit, "is:", result)

print("This program is executed by Harshit Sidher 0221BCA054")