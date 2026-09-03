# ============================================
# Palindrome Number Check
# ============================================

# --------------------------------------------
# Way 1: Iterative Check
# Time Complexity: O(log n)
# Space Complexity: O(1)
# --------------------------------------------

num = int(input("Enter a number: "))

if num < 0:
    print(num, "is NOT a Palindrome")
else:
    temp = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if temp == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")


# --------------------------------------------
# Way 2: Using a Function
# Time Complexity: O(log n)
# Space Complexity: O(1)
# --------------------------------------------

def is_palindrome(num):
    original = num
    reverse = 0
    if num < 0:
        return False
    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10
    return original == reverse

n = int(input("Enter number: "))

if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")


# --------------------------------------------
# Way 3: Using String Slicing
# Time Complexity: O(n)
# Space Complexity: O(n)
# --------------------------------------------

num = int(input("Enter a number: "))

if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
