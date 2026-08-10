# Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Way 1: Direct iteration (Brute Force)
a = [2, 7, 11, 15]          # Input array
target = 18                 # Target sum
n = len(a)                  # Length of array
for i in range(n):          # Loop through each element
    for j in range(i + 1, n): # Loop through subsequent elements
        if a[i] + a[j] == target: # Check if elements sum to target
            print([i, j])   # Print indices

# Way 2: Function-based approach (Brute Force)
def twoSum(nums, target):
    n = len(nums)           # Length of array
    for i in range(n):      # Outer loop
        for j in range(i + 1, n): # Inner loop
            if nums[i] + nums[j] == target: # Check if sum matches target
                return [i, j] # Return indices of the two numbers

a = twoSum([2, 7, 11, 15], 18) # Call function
print(a)                    # Print result