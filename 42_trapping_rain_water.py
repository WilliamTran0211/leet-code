"""
42. Trapping Rain Water - Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        res = [0] * length
        idx = 0
        max_idx = -1
        max_val = -1
        while idx <= length - 1:
            tmp_idx = idx
            if idx == 0 and height[idx] == 0:
                idx += 1
                continue
            else:
                first_num = height[idx]
                while tmp_idx < length - 1:
                    tmp_idx += 1
                    next_val = height[tmp_idx]

                    if max_val != -1 and max_idx != length - 1:
                        if max_idx < length - 1:
                            res[tmp_idx - 1] = 0
                            res[tmp_idx] = next_val - first_num
                    else:
                        if tmp_idx == length - 1 and first_num == height[idx]:
                            max_val = first_num
                            max_idx = idx
                            break
                        if next_val >= first_num:
                            first_num = next_val
                            tmp_idx = tmp_idx
                            break
                        else:
                            res[tmp_idx] += first_num - next_val

                if max_val != -1 and idx + 1 < length - 1 and idx != 0:
                    max_idx = idx
                    idx += 2
                else:
                    if tmp_idx != idx:
                        idx = tmp_idx
                    else:
                        idx += 1

        
        sum_e = sum(res)
        return sum_e


sol = Solution()

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
print("ans: ", sol.trap(height))


height = [4, 2, 0, 3, 2, 5]  # 9
print("ans: ", sol.trap(height))


height = [766, 576, 765]
print("ans: ", sol.trap(height))
