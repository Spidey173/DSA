# Question: Factorial of a Number
# Find the factorial of a non-negative integer n (n!).

# Way 1: Using a for loop
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


# Way 2: Using a while loop
n = int(input("Enter a number: "))

fact = 1
while n > 0:
    fact *= n
    n -= 1

print("Factorial =", fact)


# Way 3: Using Recursion
def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)

n = int(input("Enter a number: "))
print("Factorial of",n,"is", fact(n))


# Way 4: Using math.factorial()
import math
n = int(input("Enter a number: "))
print("Factorial of",n,"is", math.factorial(n))


# Way 5: Using a User-Defined Function (Iterative)
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

n = int(input("Enter a number: "))
print("Factorial of",n,"is", factorial(n))
