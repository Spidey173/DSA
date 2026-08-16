# Question: LeetCode 169 - Majority Element
# Given an array nums of size n, return the majority element (the element that appears more than n // 2 times).

# Way 1: Boyer-Moore Voting Algorithm (Optimal - Time: O(N), Space: O(1))
def majorityElementVoting(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

print("Way 1:", majorityElementVoting([2, 2, 1, 1, 1, 2, 2]))


# Way 2: Hash Map / Dictionary (Time: O(N), Space: O(N))
def majorityElementHash(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num

print("Way 2:", majorityElementHash([2, 2, 1, 1, 1, 2, 2]))


# Way 3: Sorting (Time: O(N log N), Space: O(1) or O(N))
def majorityElementSort(nums):
    arr = sorted(nums)  # Using sorted() to avoid modifying the input in-place
    return arr[len(arr) // 2]

print("Way 3:", majorityElementSort([2, 2, 1, 1, 1, 2, 2]))


# Way 4: Direct iteration without functions (Boyer-Moore Voting)
nums = [2, 2, 1, 1, 1, 2, 2]
candidate = None
count = 0
for num in nums:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1

print("Way 4:", candidate)
