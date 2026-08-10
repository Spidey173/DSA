# Question: LeetCode 217 - Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Way 1: Brute Force (Compare Every Pair - Time: O(N^2), Space: O(1))
def containsDuplicateBrute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

print(containsDuplicateBrute([1, 2, 3, 1]))


# Way 2: Hash Set (Optimal - Time: O(N), Space: O(N))
def containsDuplicateSet(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsDuplicateSet([1, 2, 3, 1]))


# Way 3: Dictionary / Hash Map (Time: O(N), Space: O(N))
def containsDuplicateDict(nums):
    freq = {}
    for num in nums:
        if num in freq:
            return True
        freq[num] = 1
    return False

print(containsDuplicateDict([1, 2, 3, 1]))


# Way 4: Sorting (Time: O(N log N), Space: O(N) extra or O(1) if in-place)
def containsDuplicateSort(nums):
    arr = sorted(nums)  # Using sorted() avoids modifying the original input list
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return True
    return False

print(containsDuplicateSort([1, 2, 3, 1]))


# Way 5: Pythonic Shorthand (Time: O(N), Space: O(N))
def containsDuplicateShorthand(nums):
    return len(nums) != len(set(nums))

print(containsDuplicateShorthand([1, 2, 3, 1]))
