# Question: LeetCode 509 - Fibonacci Number
# The Fibonacci numbers form a sequence where each number is the sum of the two preceding ones, starting from 0 and 1.
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Way 1: Iterative with Pythonic Tuple Unpacking (Time: O(N), Space: O(1))
def fib_iterative_pythonic(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fib_iterative_pythonic(9))


# Way 2: Iterative using a Temp Variable (Standard in C++/Java - Time: O(N), Space: O(1))
def fib_iterative_temp(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        temp = a
        a = b
        b = temp + b
    return b

print(fib_iterative_temp(9))


# Way 3: Recursive (Time: O(2^N), Space: O(N) call stack)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(9))
