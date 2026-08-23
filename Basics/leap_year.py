# Concept: Leap Year Check
# A year is a leap year if:
# 1. It is divisible by 4.
# 2. But if it is divisible by 100, it must also be divisible by 400.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
        else:
            print(year, "is NOT a Leap Year")
    else:
        print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
