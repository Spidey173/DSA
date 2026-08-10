# Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbersSet(nums):
    num_set = set(nums)
    result = []
    
    # Check all numbers from 1 to N
    for i in range(1, len(nums) + 1):
        if i not in num_set:
            result.append(i)
            
    return result

print(findDisappearedNumbersSet([4, 3, 2, 7, 8, 2, 3, 1]))