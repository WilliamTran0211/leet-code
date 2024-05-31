"""
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.

*** You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]

XOR 1 số với chính nó kết quả luôn bằng 0
 
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for n in nums:
            xor ^= n

        diff_bit = 1

        while not (xor & diff_bit):
            diff_bit = diff_bit << 1
            print(diff_bit)

        a, b = 0, 0

        for n in nums:
            if diff_bit & n:
                a = a ^ n
            else:
                b = b ^ n
            print(n, a, b)
        return [a, b]


sol = Solution()
nums = [1, 2, 1, 3, 2, 5]
print("ans: ", sol.singleNumber(nums))
