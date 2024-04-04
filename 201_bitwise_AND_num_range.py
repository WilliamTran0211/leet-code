"""
201. Bitwise AND of Numbers Range

Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:
    Input: left = 5, right = 7
    Output: 4

Example 2:
    Input: left = 0, right = 0
    Output: 0

Example 3:
    Input: left = 1, right = 2147483647
    Output: 0

bitwise AND operator: the result is 1 if BOTH bit are 1 

1 & 1 = 1
0 & 0 = 0    
1 & 0 = 0
11 & 10 = 10

"""


class Solution:
    def decimalToBinary(self, n: int) -> int:
        return bin(n).replace("0b", "")

    def binToDecimal(self, n: str) -> int:
        return int(n, 2)

    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt


sol = Solution()
left, right = 5, 7
print(sol.rangeBitwiseAnd(left, right))
