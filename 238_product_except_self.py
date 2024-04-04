"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # work around
        # curr, res = 1, []
        # for i in range(len(nums)):
        #     res.append(curr)
        #     curr *= nums[i]

        #     print(res, curr)

        # curr = 1
        # for i in range(len(nums) - 1, -1, -1):

        #     print(i)
        #     res[i] *= curr
        #     curr *= nums[i]
        #     print(res, curr)

        # return res

        length = len(nums)

        product = [1] * length

        for i in range(1, length):
            """
            For này chạy để nhân các số bên trái với nhau. Vì index=0 không có bên trái nên bắt đầu từ 1.
            Vì là phép nhân các số bên trái nên đề lấy dc hết các giá trị bên trái chỉ cần nhân với số phía trước nó

            ví dụ [5, 1, 2, 3, 4] thì khi đến vị trí cuối giá trị sẽ bằng 5 x 1 x 2 x 3 = 5 x 2 x 3 = 10 x 3



            """
            product[i] = product[i - 1] * nums[i - 1]
            print(nums[i - 1])
            print(product)

        right = nums[-1]

        for i in range(length - 2, -1, -1):
            # for này để nhân các số bên phải với nhau sau đó cập nhật số bên phải lại
            product[i] *= right
            right *= nums[i]

            print(product)
            print(right)

        return product


sol = Solution()
nums = [5, 1, 2, 3, 4]  # [24, 120, 60, 40, 30]
print(sol.productExceptSelf(nums))
