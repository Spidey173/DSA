# Find GCD of Two Numbers

# Iterative Check
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b:
    a, b = b, a % b

print("GCD is:", a)


# Using Recursion
def gcd_recursive(x, y):
    if y == 0:
        return x
    return gcd_recursive(y, x % y)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD is:", gcd_recursive(a, b))
