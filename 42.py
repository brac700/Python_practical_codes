def demonstrate_string_methods():
    sample_string = "  Hello, World!"

    # Convert to uppercase
    upper_case = sample_string.upper()
    print("Uppercase:", upper_case)

    # Convert to lowercase
    lower_case = sample_string.lower()
    print("Lowercase:", lower_case)

    # Strip leading and trailing whitespace
    stripped_string = sample_string.strip()
    print("Stripped:", stripped_string)

    # Replace a substring
    replaced_string = sample_string.replace("World", "Universe")
    print("Replaced 'World' with 'Universe':", replaced_string)

    # Split the string into a list
    split_string = sample_string.split()
    print("Split into words:", split_string)

    # Join a list of strings into a single string
    joined_string = " ".join(split_string)
    print("Joined back into a single string:", joined_string)

    # Find the position of a substring
    position = sample_string.find("World")
    print("Position of 'World':", position)

    # Count occurrences of a substring
    count = sample_string.count("o")
    print("Count of 'o':", count)

    # String formatting
    formatted_string = "Hello, {}. Welcome to {}!".format("Harshit", "Python")
    print("Formatted string:", formatted_string)

# Demonstrate string methods
demonstrate_string_methods()
print("\n This program is written and executed by Harshit Sidher (0221BCA054)")
