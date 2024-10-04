def is_palindrome(s):
    # Normalize the string: remove spaces and convert to lowercase
    normal_str = ''.join(s.split()).lower()
    
    # Use slicing to check if the string is the same forwards and backwards
    return normal_str == normal_str[::-1]

# Get user input
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")
