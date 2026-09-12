# Factorial of a Number

# Way 1: Iterative Approach
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial (Iterative):", fact)


# Way 2: Recursive Approach
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

print("Factorial (Recursive):", factorial(n))
