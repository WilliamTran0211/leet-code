"""
1208. Get Equal Substrings Within Budget
Medium
Topics
Companies
Hint
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. 
If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.

Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.

Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

chuyển chuỗi s thành t, với ký tự thứ s[i] thành t[i] sẽ tốn cost = |s[i] - t[i]| 
với s[i] và t[i] là các giá trị trong mã ASCII

Trả về max length của chuỗi con s có thể thay đổi sao cho giống với chuỗi con ở t 
với cost nhỏ hơn hoặc bằng maxCost cho trước, nếu không có trả về 0
ví dụ s = "abcd", t = "cdef", maxCost = 3
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        length = len(s)
        current_cost = 0
        l = 0
        res = 0
        for r in range(length):
            current_cost += abs(ord(t[r]) - ord(s[r]))
            while current_cost > maxCost:
                current_cost -= abs(ord(t[l]) - ord(s[l]))
                l += 1
            res = max(res, r - l + 1)

        return res


sol = Solution()
print("ans (3): ", sol.equalSubstring("abcd", "bcdf", 3))

print("ans (1): ", sol.equalSubstring("abcd", "cdef", 3))

print("ans (1): ", sol.equalSubstring("abcd", "acde", 0))

print("ans (1): ", sol.equalSubstring("vjlqwkzamvyv", "suusjpqkhlkz", 7))

print("ans (4): ", sol.equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14))
