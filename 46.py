def common_characters(str1, str2):
    # Convert both strings to sets to find unique characters
    set1 = set(str1)
    set2 = set(str2)
    
    # Find the intersection of both sets
    common_chars = set1.intersection(set2)
    
    # Print the common characters
    if common_chars:
        print("Common characters:", ' '.join(common_chars))
    else:
        print("No common characters found.")

# Get user input for the two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function to find and print common characters
common_characters(string1, string2)

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")