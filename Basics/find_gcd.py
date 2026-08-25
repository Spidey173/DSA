# Find GCD of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp_a, temp_b = a, b
while temp_b > 0:
    temp_a, temp_b = temp_b, temp_a % temp_b

print("GCD of", a, "and", b, "is", temp_a)


# Using Recursion
def gcd_recursive(x, y):
    if y == 0:
        return x
    return gcd_recursive(y, x % y)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD of", a, "and", b, "is", gcd_recursive(a, b))
