# Concept: Odd or Even
# A number is even if it is divisible by 2 (remainder is 0 when divided by 2).
# We check this using the modulo operator (%) which gives the remainder.

num = int(input("Enter a number: "))

# If remainder is 0, it is even. Otherwise, it is odd.
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
