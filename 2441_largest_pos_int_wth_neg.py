"""
2441. Largest Positive Integer That Exists With Its Negative
Given an integer array nums that does not contain any zeros, 
find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:
Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Example 2:
Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:
Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
 

"""

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        sorted_nums = sorted(nums)
        current_max = 99999999999999
        while len(sorted_nums) > 0:
            current_max = sorted_nums.pop(-1)
            if -current_max in sorted_nums:
                return current_max
        return res


sol = Solution()
nums = [-1, 2, -3, 3]
print("ans: ", sol.findMaxK(nums))


nums = [-1, 10, 6, 7, -7, 1]
print("ans: ", sol.findMaxK(nums))


nums = [-10, 8, 6, 7, -2, -3]
print("ans: ", sol.findMaxK(nums))

nums = [33, 14, 38, -13, 48, -13, -3, 44, 29, -1, 42, 20, -33, 10, -49]
print("ans: ", sol.findMaxK(nums))


nums = [-25, 25, -27, 45, 31, 46, 46, 21]
print("ans: ", sol.findMaxK(nums))
