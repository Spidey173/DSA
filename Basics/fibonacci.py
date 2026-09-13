# Fibonacci Series

# Way 1: Iterative Approach
n = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci Series (Iterative):")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# Way 2: Recursive Approach (Finding nth Fibonacci Number)
def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print(f"Nth Fibonacci number (n={n}):", fibonacci(n))
