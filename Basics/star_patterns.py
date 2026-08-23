# Concept: Nested Loops / Star Patterns
# Printing patterns helps build a strong logical understanding of nested loops.

rows = int(input("Enter number of rows: "))

print("\n--- Pattern 1: Right-Angle Triangle ---")
# Outer loop controls rows
for i in range(1, rows + 1):
    # Inner loop prints stars for each row
    for j in range(i):
        print("*", end="")
    print()  # Move to next line after printing a row


print("\n--- Pattern 2: Inverted Right-Angle Triangle ---")
# Outer loop starts at max rows and decreases
for i in range(rows, 0, -1):
    # Inner loop prints stars
    for j in range(i):
        print("*", end="")
    print()
