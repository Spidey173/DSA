# Find GCD of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp_a, temp_b = a, b
while temp_b > 0:
    temp_a, temp_b = temp_b, temp_a % temp_b

print("GCD of", a, "and", b, "is", temp_a)
