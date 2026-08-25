# Count Digits in a Number

num = int(input("Enter a number: "))
count = 0
temp = num

while temp > 0:
    temp //= 10
    count += 1

print("Number of digits:", count)


# Using Recursion
def count_recursive(n):
    if n == 0:
        return 0
    return 1 + count_recursive(n // 10)

num = int(input("Enter a number: "))
print("Number of digits:", count_recursive(num))
