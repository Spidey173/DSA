# Armstrong Number Check

# Way 1: Iterative Check (Time: O(log n), Space: O(1))
num = int(input("Enter a number: "))
power = len(str(num))
temp = num
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** power
    temp //= 10

if sum_val == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# Way 2: Recursive Check (Time: O(log n), Space: O(log n) call stack)
def armstrong_sum(n, power):
    if n == 0:
        return 0
    return ((n % 10) ** power) + armstrong_sum(n // 10, power)

num = int(input("Enter a number: "))
power = len(str(num))

if armstrong_sum(num, power) == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
