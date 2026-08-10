# Question: LeetCode 217 - Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Way 1: Hash Set (Optimal - Time: O(N), Space: O(N))
# This is the best general interview solution because it has an early exit.
def containsDuplicateSet(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print("Way 1 (Set) [1, 2, 3, 1]:", containsDuplicateSet([1, 2, 3, 1]))
print("Way 1 (Set) [1, 2, 3, 4]:", containsDuplicateSet([1, 2, 3, 4]))


# Way 2: Sorting (Space Optimized - Time: O(N log N), Space: O(1))
# Use this if the interviewer restricts memory usage (O(1) auxiliary space).
def containsDuplicateSort(nums):
    nums.sort()  # Sorts the array in-place
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

print("Way 2 (Sort) [1, 2, 3, 1]:", containsDuplicateSort([1, 2, 3, 1]))
print("Way 2 (Sort) [1, 2, 3, 4]:", containsDuplicateSort([1, 2, 3, 4]))


# Way 3: Pythonic Shorthand (Time: O(N), Space: O(N))
# Good to mention as a quick Python-specific approach.
def containsDuplicateShorthand(nums):
    return len(nums) != len(set(nums))

print("Way 3 (Shorthand) [1, 2, 3, 1]:", containsDuplicateShorthand([1, 2, 3, 1]))
print("Way 3 (Shorthand) [1, 2, 3, 4]:", containsDuplicateShorthand([1, 2, 3, 4]))
