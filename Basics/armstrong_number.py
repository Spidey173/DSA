# Armstrong Number Check

# Way 1: Iterative Check (Time: O(log n), Space: O(1))
num1 = int(input("Enter a number: "))
power1 = len(str(num1))
temp = num1
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** power1
    temp //= 10

if sum_val == num1:
    print("Way 1:", num1, "is an Armstrong number")
else:
    print("Way 1:", num1, "is not an Armstrong number")


# Way 2: Recursive Check (Time: O(log n), Space: O(log n) call stack)
def armstrong_sum(n, power):
    if n == 0:
        return 0
    return ((n % 10) ** power) + armstrong_sum(n // 10, power)

num2 = int(input("Enter a number: "))
power2 = len(str(num2))

if armstrong_sum(num2, power2) == num2:
    print("Way 2:", num2, "is an Armstrong number")
else:
    print("Way 2:", num2, "is not an Armstrong number")
