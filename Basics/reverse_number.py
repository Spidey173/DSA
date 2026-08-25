# Reverse a Number

# Way 1: Iterative Loop (Simplest for positive numbers)
num1 = int(input("Enter a number: "))
reverse = 0
temp1 = num1

while temp1 > 0:
    digit = temp1 % 10
    reverse = reverse * 10 + digit
    temp1 //= 10

print("Way 1 Reversed:", reverse)


# Way 2: Using Recursion
def reverse_recursive(n, rev=0):
    if n == 0:
        return rev
    return reverse_recursive(n // 10, rev * 10 + (n % 10))

num2 = int(input("Enter a number: "))
print("Way 2 Reversed:", reverse_recursive(num2))
