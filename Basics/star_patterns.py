# Star Patterns

rows = int(input("Enter number of rows: "))

print("\n--- Pattern 1: Right-Angle Triangle ---")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\n--- Pattern 2: Inverted Right-Angle Triangle ---")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
