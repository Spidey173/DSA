# Concept: Prime Number Check
# A prime number is a number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# Example: 2, 3, 5, 7, 11... (divided only by 1 and itself).

num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    # Check divisors from 2 up to num - 1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Found a divisor, so it's not prime
            break

if is_prime:
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
