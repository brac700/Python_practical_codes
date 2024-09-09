try:
    number = int(input("Enter a number: "))
    result = 10/number
except ZeroDivisionError:
    print("Division by zero is not possible.")
except ValueError:
    print("Invalid input.")
    
print("Written and executed by Harshit Sidher(0221BCA054)")