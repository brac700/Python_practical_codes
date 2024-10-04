def string_traversing(s):
    # Initialize counters for vowels and consonants
    vowels_count = 0
    consonants_count = 0
    vowels = "aeiouAEIOU"

    print("Traversing the string:")
    for char in s:
        print(char, end=' ')  # Print each character in the string
        
        # Check if the character is a vowel or a consonant
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    print("\n\nTotal Vowels:", vowels_count)
    print("Total Consonants:", consonants_count)

# Get user input
input_string = input("Enter a string: ")
string_traversing(input_string)

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")