# Count Digits in a Number

num = int(input("Enter a number: "))
temp = abs(num)  # Handle negative numbers
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print("Number of digits:", count)
