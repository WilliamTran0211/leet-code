"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2: 
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        # Handle edge cases efficiently
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return length

        # this while loop is Binary search for middle points
        low, high = 0, length - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

        # max_val = nums[-1]
        # min_val = nums[0]

        # if target >= max_val:
        #     return length
        # elif target <= min_val:
        #     return 0
        # else:
        #     half_idx = length // 2

        #     half_val = nums[half_idx]

        #     if target >= half_val:
        #  this 2 for is O(n) because it can be loops for half of the list so it is O(n)
        #         for i, ele in enumerate(nums, half_idx):
        #             if nums[i] >= target:
        #                 return half_idx
        #             if nums[i + 1] >= target:
        #                 return half_idx + 1
        #     else:
        #         for i, ele in enumerate(nums, start=0, end=half_val):
        #             if nums[i] >= target:
        #                 return i
        #             else:
        #                 return i + 1


sol = Solution()


nums, target = [1, 3, 5, 6], 5
print("ans:  ", sol.searchInsert(nums, target))

nums, target = [1, 3, 5, 6], 2
print("ans:  ", sol.searchInsert(nums, target))

nums, target = [1, 3, 5, 6, 7, 9], 7
print("ans:  ", sol.searchInsert(nums, target))
