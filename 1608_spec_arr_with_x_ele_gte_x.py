"""
1608. Special Array With X Elements Greater Than or Equal X
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

tìm số X sao cho có chính xác X số lớn hơn hoặc bằng X trong mảng cho trước 
Nếu tìm dc số X đó thì số X có thể không có trong mảng cũng như X là duy nhất.
"""

from typing import List
from collections import Counter, OrderedDict


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        res = -1

        n_cnt = Counter(nums)

        for i in range(0, len(nums) + 1):
            pop = 0
            if i in n_cnt.keys():
                pop = n_cnt.pop(i)

            greater_equal_i = pop + sum(n_cnt.values())
            if i == greater_equal_i:
                res = i
                break

        return res


sol = Solution()
nums = [1, 4, 3, 1, 4]
print("ans: ", sol.specialArray(nums))

nums = [0, 0]
print("ans: ", sol.specialArray(nums))

nums = [3, 5]
print("ans: ", sol.specialArray(nums))

nums = [3, 9, 7, 8, 3, 8, 6, 6]
print("ans (must be 6): ", sol.specialArray(nums))

nums = [3, 6, 7, 7, 0]
print("ans (must be -1): ", sol.specialArray(nums))


nums = [
    11,
    0,
    15,
    16,
    1,
    6,
    6,
    14,
    25,
    23,
    24,
    25,
    26,
    7,
    16,
    1,
    16,
    16,
    15,
    24,
    27,
    18,
    12,
    26,
    16,
]
print("ans (must be -1): ", sol.specialArray(nums))
