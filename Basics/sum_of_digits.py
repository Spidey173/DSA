# Sum of Digits

num = int(input("Enter a number: "))
temp = abs(num)
digit_sum = 0

while temp > 0:
    last_digit = temp % 10
    digit_sum += last_digit
    temp //= 10

print("Sum of digits:", digit_sum)
