"""
633. Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

theo yêu cầu a * a + b * b = c

vì vậy 0 <= a, b <= c
do đó 0 <= a^2, b^2 <= c

vì vậy 0 <= a, b <= √c


tiếp cận:
tính hết các giá trị của b^2 từ 0 đến √c
đưa các giá trị vào set
sau đó tính các giá trị của √(a^2 - c) (*) từ 0 đến √c
và tìm kiếm giá trị trong set

(*) khai triển từ a^2 + b^2 = c => b^2 = a^2 - c
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        set_b = set()

        for b in range(int(math.sqrt(c)) + 1):
            set_b.add(b * b)

        a = 0
        while a * a <= c:
            target_b = abs((a * a) - c)
            if target_b in set_b:
                return True
            a += 1

        return False


sol = Solution()
print("ans: ", sol.judgeSquareSum(5))

print("ans: ", sol.judgeSquareSum(3))

print("ans: ", sol.judgeSquareSum(9))  # 0^2 + 3^2 = 0 * 0 + 3 * 3= 9

print("ans: ", sol.judgeSquareSum(15))
