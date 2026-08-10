# Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Way 1: Direct iteration (Brute Force)
a = [2, 7, 11, 15]
target = 18
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == target:
            print([i, j])

# Way 2: Function-based approach (Brute Force)
def twoSum(nums, target):
    ans = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                ans.append([i, j])

    return ans

print(twoSum([1,2,3,4,5], 5))