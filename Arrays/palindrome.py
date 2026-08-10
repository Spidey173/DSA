# Question: Palindrome Check
# Check if a given string or list is a palindrome (reads the same forwards and backwards).

# Way 1: Two Pointers Comparison (Time: O(N), Space: O(1))
def is_palindrome_loop(arr):
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            return False
    return True

print(is_palindrome_loop("madam"))


# Way 2: Slicing Shorthand (Time: O(N), Space: O(N) copy)
def is_palindrome_slicing(arr):
    return arr == arr[::-1]

print(is_palindrome_slicing(['m', 'a', 'd', 'a', 'm']))
