def string_operations():
    # Initialize a string
    my_string = "  Hello, World!"

    # Display the original string
    print("Original String:", my_string)

    # 1. Convert to uppercase
    upper_case = my_string.upper()
    print("Uppercase:", upper_case)

    # 2. Convert to lowercase
    lower_case = my_string.lower()
    print("Lowercase:", lower_case)

    # 3. Strip leading and trailing whitespace
    stripped_string = my_string.strip()
    print("Stripped:", stripped_string)

    # 4. Replace a substring
    replaced_string = my_string.replace("World", "Universe")
    print("Replaced 'World' with 'Universe':", replaced_string)

    # 5. Split the string into a list
    split_string = my_string.split()
    print("Split into words:", split_string)

    # 6. Join a list of strings into a single string
    joined_string = " ".join(split_string)
    print("Joined back into a single string:", joined_string)

    # 7. Find the position of a substring
    position = my_string.find("World")
    print("Position of 'World':", position)

    # 8. Count occurrences of a substring
    count = my_string.count("o")
    print("Count of 'o':", count)

    # 9. String formatting using f-strings
    name = "Harshit"
    language = "Python"
    formatted_string = f"Hello, {name}. Welcome to {language}!"
    print("Formatted string (f-string):", formatted_string)

    # 10. Demonstrating raw strings
    raw_string = r"C:\Users\Name\Documents\Folder"
    print("Raw string:", raw_string)

# Run the string operations
string_operations()

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")