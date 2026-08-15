# Question: Reverse a String
# Given a string s, return its reversed version.

# Way 1: Recursion with Slicing (Time: O(N^2) due to slicing, Space: O(N) stack depth)
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

print(reverse_recursive("hello"))


# Way 2: Recursion with Two Pointers / Helper (Time: O(N), Space: O(N) stack depth)
def reverse_recursive_helper(chars, left, right):
    if left >= right:
        return
    chars[left], chars[right] = chars[right], chars[left]  # Swap
    reverse_recursive_helper(chars, left + 1, right - 1)

def reverse_recursive_two_pointers(s):
    chars = list(s)
    reverse_recursive_helper(chars, 0, len(chars) - 1)
    return "".join(chars)

print(reverse_recursive_two_pointers("hello"))


# Way 3: Iterative Two Pointers (Optimal - Time: O(N), Space: O(N) to convert string to mutable list)
def reverse_two_pointers(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]  # Swap
        left += 1
        right -= 1
    return "".join(chars)

print(reverse_two_pointers("hello"))


# Way 4: Backward Loop (Time: O(N), Space: O(N))
s4 = "hello"
rev4 = ""
for i in range(len(s4) - 1, -1, -1):
    rev4 += s4[i]

print(rev4)


# Way 5: Prepending Loop (Time: O(N^2) due to string concatenation overhead, Space: O(N))
s5 = "hello"
rev5 = ""
for ch in s5:
    rev5 = ch + rev5

print(rev5)


# Way 6: Slicing Shorthand (Optimal Pythonic - Time: O(N), Space: O(N))
s6 = "hello"
rev6 = s6[::-1]

print(rev6)


# Way 7: Using reversed() and join() (Time: O(N), Space: O(N))
s7 = "hello"
rev7 = "".join(reversed(s7))

print(rev7)
