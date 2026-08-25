# Reverse a Number

num = int(input("Enter a number: "))
temp = abs(num)
reversed_num = 0

while temp > 0:
    last_digit = temp % 10
    reversed_num = (reversed_num * 10) + last_digit
    temp //= 10

if num < 0:
    reversed_num = -reversed_num

print("Reversed number:", reversed_num)
