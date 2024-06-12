"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

0: red
1: white
2: blue

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""

from typing import List
from collections import defaultdict


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # brute force in my way
        history = defaultdict(int)

        for n in nums:
            history[n] += 1

        new_list = []
        new_list.extend([0] * history[0])
        new_list.extend([1] * history[1])
        new_list.extend([2] * history[2])

        nums.clear()
        nums.extend(new_list)

        # optimize do quick sort


sol = Solution()
nums = [2, 0, 2, 1, 1, 0]
print(sol.sortColors(nums))
