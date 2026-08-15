# Question: Fizz Buzz
# Print numbers from 1 to n. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", 
# and for multiples of both 3 and 5 print "FizzBuzz".

# Way 1: Basic if-elif-else (using modulo 15)
print("--- Way 1: Basic % 15 ---")
n = 20
for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Way 2: Basic checking 3 and 5 separately
print("\n--- Way 2: Checking 3 and 5 separately ---")
n = 20
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Way 3: Using String Concatenation (Using 'or' shorthand)
print("\n--- Way 3: String Concatenation (Using 'or') ---")
n = 20
for i in range(1, n + 1):
    ans = ""
    if i % 3 == 0:
        ans += "Fizz"
    if i % 5 == 0:
        ans += "Buzz"
    print(ans or i)


# Way 4: String Concatenation (Using 'if-else')
print("\n--- Way 4: String Concatenation (Using 'if-else') ---")
n = 20
for i in range(1, n + 1):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    print(result if result else i)


# Way 5: Ternary Operator (One-liner print)
print("\n--- Way 5: Ternary Operator ---")
n = 20
for i in range(1, n + 1):
    print("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)


# Way 6: Using a User-Defined Function
print("\n--- Way 6: Using Function ---")
def fizzbuzz_func(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    return x

n = 20
for i in range(1, n + 1):
    print(fizzbuzz_func(i))


# Way 7: Using a While Loop
print("\n--- Way 7: While Loop ---")
n = 20
i = 1
while i <= n:
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
