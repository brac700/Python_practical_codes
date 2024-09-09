def is_perfect(num):
  """Checks if a number is perfect."""
  divisors = [i for i in range(1, num) if num % i == 0]
  return sum(divisors) == num

def print_first_n_perfect(n):
  """Prints the first n perfect numbers."""
  count = 0
  num = 1

  while count < n:
    if is_perfect(num):
      print(num)
      count += 1
    num += 1

# Get the number of perfect numbers to print from the user
n = int(input("Enter the number of perfect numbers to print: "))

print_first_n_perfect(n)

print("Written and demonstrated by Harshit Sidher (0221BCA054)")