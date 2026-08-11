# Question: Palindrome Check
# Check if a given string is a palindrome (reads the same forwards and backwards).

# Way 1: Two Pointers Comparison (Time: O(N), Space: O(1))
def is_palindrome_loop(arr):
    arr = arr.lower()
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            return False
    return True

print(is_palindrome_loop("Madam"))


# Way 2: Slicing Shorthand (Time: O(N), Space: O(N) copy)
def is_palindrome_slicing(arr):
    arr = arr.lower()
    return arr == arr[::-1]

print(is_palindrome_slicing("Madam"))

# Way 3: Direct iteration without functions or slicing
s = input("Enter a string: ")
s = s.lower()
n = len(s)
is_palindrome = True
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_palindrome = False
        break

print(is_palindrome)
