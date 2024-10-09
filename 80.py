#positional parameter
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30)

#default parameter
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30)
greet("Alice")

#keyword parameter
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", age=30)
greet(age=30, name = "Alice")

#variable length parameter - args
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1,2,3))
print(sum_numbers(4,5,6,7,8))

#variable length parameter - kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_info(name = "Alice", age = 30, city = "New York")

print("\n This program is written and executed by Harshit Sidher (0221BCA054)")