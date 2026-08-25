# Find LCM of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp_a, temp_b = a, b
while temp_b > 0:
    temp_a, temp_b = temp_b, temp_a % temp_b

gcd = temp_a
lcm = (a * b) // gcd

print("LCM of", a, "and", b, "is", lcm)
