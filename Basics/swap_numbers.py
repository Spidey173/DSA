# Swap Two Numbers

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Way 1: Using a temporary variable
temp = a
a = b
b = temp
print("After swap (Way 1) -> a =", a, ", b =", b)

# Way 2: Pythonic shorthand (without temp variable)
a, b = b, a
print("After swap (Way 2) -> a =", a, ", b =", b)
