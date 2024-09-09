num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
num3 = input("Enter num3: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if (num1 > num2) and (num1 > num3):
    print(f"Num1 is the largest. Value: {num1}")
elif (num2 > num1) and (num2 > num3):
    print(f"Num2 is the largest. Value: {num2}")
else:
    print(f"Num3 is the largest. Value: {num3}")
    
print("This program is written and demonstrated by Harshit Sidher (0221BCA054)")