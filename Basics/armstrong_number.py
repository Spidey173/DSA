# Armstrong Number Check

num = int(input("Enter a number: "))

# Find the number of digits
power = len(str(num))

# Calculate the sum of digits raised to the power
temp = num
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** power
    temp //= 10

# Check Armstrong number
if sum_val == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
