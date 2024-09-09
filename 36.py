def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == num


low_limit = int(input("Enter the lower limit of the range you wish to check for Armstrong numbers: "))
upp_limit = int(input("Enter the upper limit of the range you wish to check for Armstrong numbers: "))

counter = 0

for i in range(low_limit, upp_limit):
    if is_armstrong(i):
        print(i)
        counter = counter + 1
print(f"Counter: {counter}")


print("Written and executed by Harshit Sidher 0221BCA054")

