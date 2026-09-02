# Find LCM of Two Numbers

# Iterative (Using GCD Formula)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp_a, temp_b = a, b
while temp_b:
    temp_a, temp_b = temp_b, temp_a % temp_b

lcm = (a * b) // temp_a
print("LCM of", a, "and", b, "is", lcm)


# Using Recursion
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = (a * b) // gcd(a, b)
print("LCM of", a, "and", b, "is", lcm)
