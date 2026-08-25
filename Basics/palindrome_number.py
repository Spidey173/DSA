# Palindrome Number Check

# Way 1: Iterative Check (Time: O(log n), Space: O(1))
num1 = int(input("Enter a number: "))

if num1 < 0:
    print("Way 1:", num1, "is NOT a Palindrome")
else:
    temp = num1
    reversed_num = 0
    while temp > 0:
        last_digit = temp % 10
        reversed_num = (reversed_num * 10) + last_digit
        temp //= 10
        
    if num1 == reversed_num:
        print("Way 1:", num1, "is a Palindrome")
    else:
        print("Way 1:", num1, "is NOT a Palindrome")


# Way 2: Recursive Check (Time: O(log n), Space: O(log n) call stack)
def reverse_recursive(n, rev=0):
    if n == 0:
        return rev
    return reverse_recursive(n // 10, rev * 10 + (n % 10))

def is_palindrome_recursive(num):
    if num < 0:
        return False
    return num == reverse_recursive(num)

num2 = int(input("Enter a number: "))
if is_palindrome_recursive(num2):
    print("Way 2:", num2, "is a Palindrome")
else:
    print("Way 2:", num2, "is NOT a Palindrome")
