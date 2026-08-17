# Question: Merge Sorted Arrays
# 1. Standard Merge: Merge two sorted arrays into a new sorted array.
# 2. In-Place Merge: Merge nums2 into nums1 in-place where nums1 has placeholder space.

# Way 1: Two Pointers Standard Merge (Time: O(N+M), Space: O(N+M))
def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

print("Way 1:", merge_sorted([1, 3, 5], [2, 4, 6]))


# Way 2: In-Place Merge (Time: O(N+M), Space: O(1))
def merge_inplace(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1

print("Way 2:", merge_inplace([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


# Way 3: Direct iteration without functions (Standard Two-Pointer)
a = [1, 3, 5]
b = [2, 4, 6]
i = j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

while i < len(a):
    result.append(a[i])
    i += 1

while j < len(b):
    result.append(b[j])
    j += 1

print("Way 3:", result)


# Way 4: Direct iteration without functions (In-Place Merge)
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print("Way 4:", nums1)


# Way 5: Concatenate and Sort (Simplest way - Time: O((N+M) log(N+M)), Space: O(N+M))
a_simple = [1, 3, 5]
b_simple = [2, 4, 6]
result_simple = sorted(a_simple + b_simple)
print("Way 5 (Simplest):", result_simple)
