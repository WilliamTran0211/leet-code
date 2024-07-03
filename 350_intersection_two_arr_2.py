"""
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_cnt = Counter(nums1)
        num2_cnt = Counter(nums2)
        res = []
        for ele, cnt in num1_cnt.items():
            if ele in num2_cnt:
                num2_c = num2_cnt[ele]
                quan = num2_c if num2_c == cnt else cnt if num2_c > cnt else num2_c
                res.extend([ele] * quan)

        return res


sol = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print("ans ", sol.intersect(nums1, nums2))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print("ans ", sol.intersect(nums1, nums2))


nums1 = [1, 2]
nums2 = [1, 1]

print("ans ", sol.intersect(nums1, nums2))
