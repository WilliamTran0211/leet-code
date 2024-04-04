"""
442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice,
return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

this line important: "...all the integers of nums are in the range [1, n]..." 


"uses only constant extra space" câu này nghĩa là chỉ dc 1 mảng đầu vào duy nhất, xử lý nó và trả về mảng đó mà không tạo ra mảng mới

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums.clear()
        else:
            res = []
            for idx, ele in enumerate(nums):

                new_idx = abs(ele) - 1

                if nums[new_idx] < 0:
                    res.append(abs(ele))
                else:
                    nums[new_idx] = -nums[new_idx]

        return res


sol = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(sol.findDuplicates(nums))

nums = [4, 3, 2, 7, 8, 2, 3, 1, 1]
print(sol.findDuplicates(nums))

# nums = [1, 1, 2]
# print(sol.findDuplicates(nums))

# nums = [1]
# print(sol.findDuplicates(nums))
