# Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Way 1: Direct iteration (Brute Force - print directly)
a = [2, 7, 11, 15]
target = 18
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == target:
            print([i, j])

# Way 2: Direct iteration using break to print only one outcome
a = [1, 2, 3, 4, 5]
target = 5
n = len(a)
found = False
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == target:
            print([i, j])
            found = True
            break
    if found:
        break

# Way 3: Function returning all possible outcomes
def twoSumAll(nums, target):
    ans = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                ans.append([i, j])
    return ans

print(twoSumAll([1, 2, 3, 4, 5], 5))

# Way 4: Function returning only the 1st outcome (using return statement)
def twoSumFirst(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSumFirst([1, 2, 3, 4, 5], 5))