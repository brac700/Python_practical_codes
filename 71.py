#Program to Access and Remove Dictionary Elements
my_dict = {'name': 'Bob', 'age': 30, 'job': 'Engineer'}  # Remove the space in 'Engineer'
name = my_dict.get('name')  # Get the value associated with the key 'name'
my_dict.pop('job')  # Remove the key 'job' from the dictionary

# Print the results
print(name)  # Outputs: Bob
print(my_dict)  # Outputs: {'name': 'Bob', 'age': 30}

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")