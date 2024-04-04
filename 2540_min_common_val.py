"""
2540. Minimum Common Value

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
return the minimum integer common to both arrays. 
If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 
if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, 
so 2 is returned.

"""

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num_set1 = set(nums1)
        num_set2 = set(nums2)

        # not_in_both = num_set1.symmetric_difference(
        #     nums2
        # )  # lấy phần không giao giữa 2 tập hợp

        # print(not_in_both)

        in_both = num_set1.intersection(num_set2) #lấy phần giao

        return min(in_both) if len(in_both) > 0 else -1


sol = Solution()

nums1 = [1, 2, 3]
nums2 = [2, 4]
print(sol.getCommon(nums1, nums2))

nums1 = [1, 2, 3, 6]
nums2 = [2, 3, 4, 5]
print(sol.getCommon(nums1, nums2))

nums1 = [100, 200, 300]
nums2 = [50, 100, 150, 200]
print(sol.getCommon(nums1, nums2))

nums1 = [2, 4, 6, 8, 10]
nums2 = [1, 3, 5, 7, 9]
print(sol.getCommon(nums1, nums2))
