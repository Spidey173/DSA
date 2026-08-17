# Question: Intersection of Two Arrays (Common Elements)
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

# Way 1: Hash Set (Optimal - Time: O(N + M), Space: O(N))
def intersection_set(nums1, nums2):
    set1 = set(nums1)
    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)
    return list(result)

print(intersection_set([1, 2, 2, 1], [2, 2]))


# Way 2: Two Pointers and Sorting (Time: O(N log N + M log M), Space: O(1) auxiliary)
def intersection_pointers(nums1, nums2):
    nums1.sort()
    nums2.sort()
    left, right = 0, 0
    result = set()
    
    while left < len(nums1) and right < len(nums2):
        if nums1[left] == nums2[right]:
            result.add(nums1[left])
            left += 1
            right += 1
        elif nums1[left] < nums2[right]:
            left += 1
        else:
            right += 1
            
    return list(result)

print(intersection_pointers([1, 2, 2, 1], [2, 2]))


# Way 3: Pythonic Shorthand (Time: O(N + M), Space: O(N + M))
def intersection_shorthand(nums1, nums2):
    return list(set(nums1) & set(nums2))

print(intersection_shorthand([1, 2, 2, 1], [2, 2]))
