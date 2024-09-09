bill = int(input("Enter the bill amount in INR: "))

def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number //= 10
    return sum_digits

if bill > 10000:
    discount_percentage = sum_of_digits(bill) / 2
else:
    discount_percentage = sum_of_digits(bill)

discount_amount = (discount_percentage / 100) * bill
final_bill = bill - discount_amount

print(f"Discount percentage: {discount_percentage}%")
print(f"Discount amount: {discount_amount}")
print(f"Final amount to be paid: {final_bill}")


print("This program is written and executed by Harshit Sidher (0221BCA054)")

