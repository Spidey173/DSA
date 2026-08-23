# Armstrong Number Check

num = int(input("Enter a number: "))
temp = num
num_str = str(num)
num_digits = len(num_str)
sum_powers = 0

while temp > 0:
    digit = temp % 10
    sum_powers += digit ** num_digits
    temp //= 10

if sum_powers == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
