"""
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

"""

from typing import List


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:

        nums = sorted(nums)

        max_nums = nums[-1]

        for idx, n in enumerate(nums):

            if idx != n:
                return idx

        return max_nums + 1

    def missingNumber2(self, nums: List[int]) -> int:

        arr_len = len(nums)

        total_arr = sum(nums)

        total_sum = (arr_len * (arr_len + 1)) // 2

        return total_sum - total_arr


sol = Solution()

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print(sol.missingNumber1(nums))
print(sol.missingNumber2(nums))
