# Palindrome Number Check

num = int(input("Enter a number: "))

if num < 0:
    print(num, "is NOT a Palindrome")
else:
    temp = num
    reversed_num = 0
    
    while temp > 0:
        last_digit = temp % 10
        reversed_num = (reversed_num * 10) + last_digit
        temp //= 10
        
    if num == reversed_num:
        print(num, "is a Palindrome")
    else:
        print(num, "is NOT a Palindrome")
