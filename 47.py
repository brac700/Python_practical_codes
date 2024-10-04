def count_characters(s):
    # Initialize counters
    vowels_count = 0
    consonants_count = 0
    blanks_count = 0
    vowels = "aeiouAEIOU"  # Define vowels

    # Traverse the string
    for char in s:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowels_count += 1  # Increment vowel count
            else:
                consonants_count += 1  # Increment consonant count
        elif char == ' ':
            blanks_count += 1  # Increment blank count

    # Print the results
    print("Total Vowels:", vowels_count)
    print("Total Consonants:", consonants_count)
    print("Total Blanks (Spaces):", blanks_count)

# Get user input
input_string = input("Enter a string: ")
count_characters(input_string)


print("\n This program is written and executed by Harshit Sidher (0221BCA054)")