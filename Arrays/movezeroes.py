# Question: LeetCode 283 - Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Must do this in-place.

# Way 1: Two-Pointer Swap (Time: O(N), Space: O(1))
def moveZeroesSwap(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

nums1 = [0, 1, 0, 3, 12]
moveZeroesSwap(nums1)
print("Way 1:", nums1)


# Way 2: Overwrite and Fill (Time: O(N), Space: O(1))
def moveZeroesFill(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    while index < len(nums):
        nums[index] = 0
        index += 1

nums2 = [0, 1, 0, 3, 12]
moveZeroesFill(nums2)
print("Way 2:", nums2)


# Way 3: Direct iteration without functions
nums3 = [0, 1, 0, 3, 12]
left = 0
for right in range(len(nums3)):
    if nums3[right] != 0:
        nums3[left], nums3[right] = nums3[right], nums3[left]
        left += 1

print("Way 3:", nums3)
