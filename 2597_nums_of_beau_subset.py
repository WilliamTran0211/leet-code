"""
2597. The Number of Beautiful Subsets\
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. 
Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

trong mảng kết quả không dc có phần từ mà khi lấy nó cộng cho K xuất hiện trong mảng ban đầu.
Mảng con đó sẽ là beautiful
"""

from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def helper(i, count):
            if i == len(nums):
                return 1

            res = helper(i + 1, count)

            if not count[nums[i] + k] and not count[nums[i] - k]:
                count[nums[i]] += 1
                res += helper(i + 1, count)
                count[nums[i]] -= 1

            return res

        return helper(0, defaultdict(int)) - 1


sol = Solution()
nums = [2, 4, 6]
k = 2
print(sol.beautifulSubsets(nums, k))
