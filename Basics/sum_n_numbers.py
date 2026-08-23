# Sum of N Natural Numbers

n = int(input("Enter N: "))

# Way 1: Using a for loop
sum_for = 0
for i in range(1, n + 1):
    sum_for += i
print("Way 1 (For Loop) Sum =", sum_for)

# Way 2: Using a while loop
sum_while = 0
i = 1
while i <= n:
    sum_while += i
    i += 1
print("Way 2 (While Loop) Sum =", sum_while)

# Way 3: Using the formula
sum_formula = n * (n + 1) // 2
print("Way 3 (Formula) Sum =", sum_formula)
