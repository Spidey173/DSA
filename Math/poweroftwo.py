# Question: Power of Two
# Given an integer n, return True if it is a power of two. Otherwise, return False.

# Way 1: Division by 2 (Iterative - Time: O(log n), Space: O(1))
def is_power_of_two_division(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

print("Way 1:", is_power_of_two_division(16))


# Way 2: Bitwise Trick (Optimal - Time: O(1), Space: O(1))
def is_power_of_two_bitwise(n):
    return n > 0 and (n & (n - 1)) == 0

print("Way 2:", is_power_of_two_bitwise(16))


# Way 3: Recursive Solution (Time: O(log n), Space: O(log n) call stack)
def is_power_of_two_recursive(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return is_power_of_two_recursive(n // 2)

print("Way 3:", is_power_of_two_recursive(16))


# Way 4: Loop with Multiplication (Time: O(log n), Space: O(1))
def is_power_of_two_multiplication(n):
    if n <= 0:
        return False
    power = 1
    while power < n:
        power *= 2
    return power == n

print("Way 4:", is_power_of_two_multiplication(16))


# Way 5: Direct iteration without functions (Bitwise)
n = 16
is_power = n > 0 and (n & (n - 1)) == 0
print("Way 5:", is_power)
