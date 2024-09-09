#Program to demonstrate 5 built-in functions in python

#Step 1: Get input from the user

user_input = input("Enter a list of numbers seperated by spaces: ")

input_list = user_input.split()

numbers = list(map(int, input_list))

total = sum(numbers)

length = len(numbers)

sorted_nummbers = sorted(numbers)

print(f"Original list: {numbers}")
print(f"Sum: {total}")
print(f"No. of elements: {length}")
print(f"Sorted list of numbers: {sorted_nummbers}")

print("This code was written and demonstrated by Harshit Sidher (0221BCA054)")
