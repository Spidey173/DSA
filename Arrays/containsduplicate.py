# Question: LeetCode 217 - Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Way 1: Brute Force (Compare Every Pair - Time: O(N^2), Space: O(1))
def duplicate_brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

print(duplicate_brute([1, 2, 3, 1]))


# Way 2: Hash Set (Optimal - Time: O(N), Space: O(N))
def duplicate_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(duplicate_set([1, 2, 3, 1]))


# Way 3: Pythonic Shorthand (Time: O(N), Space: O(N))
def duplicate_shorthand(nums):
    return len(nums) != len(set(nums))

print(duplicate_shorthand([1, 2, 3, 1]))
