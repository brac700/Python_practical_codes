my_string = "Bharati"
char_to_find = input("Enter the char value that you wish to find: ")
positions = [i for i, char in enumerate(my_string) if char == char_to_find]

if positions:
    print(f"The character '{char_to_find}' is found at positions {positions}")
else:
    print(f"The character '{char_to_find}' is not found in the string '{my_string}'")

print("This code was written and demonstrated by Harshit Sidher (0221BCA054)")