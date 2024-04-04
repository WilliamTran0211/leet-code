nums = [1, 2, 3, 1]
k = 3  # True

# nums = [1, 2, 3, 1, 2, 3]
# k = 2

nums = [1, 0, 1, 1]
k = 1

# s = [99, 99]
# k = 2

# nums = [1]
# k = 2

# nums = [1, 2]
# k = 2


"""
219. Contains Duplicate II
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
log = {}
for idx, i in enumerate(nums):
    if i in log:
        log[i].append(idx)
    else:
        log[i] = [idx]



