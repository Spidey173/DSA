# Question: Maximum Subarray (Kadane's Algorithm)
# Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Way 1: Kadane's Algorithm using max() (Time: O(N), Space: O(1))
class Solution1:
    def maxSubArray(self, nums):
        curr = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)

        return best

sol1 = Solution1()
print(sol1.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# Way 2: Kadane's Algorithm (Interview-Friendly - Time: O(N), Space: O(1))
class Solution2:
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum

sol2 = Solution2()
print(sol2.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Way 3: Direct iteration without classes or functions
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = float('-inf')
curr_sum = 0

for num in nums:
    curr_sum += num
    max_sum = max(max_sum, curr_sum)
    if curr_sum < 0:
        curr_sum = 0

print(max_sum)
