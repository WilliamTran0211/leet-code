"""
2370. Longest Ideal Subsequence
You are given a string s consisting of lowercase letters and an integer k. 
We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

Example 1:
Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

Example 2:
Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.


1 chuỗi t là "LÝ TƯỞNG" khi

+ t là chuỗi con* của s
+ 2 ký tự liền kề trong t, luôn nhỏ hơn hoặc bằng k theo thứ tự của ký tự đó trong bản chữ cái

*chuỗi con của s: nghĩa là 1 chuỗi có thể tạo bằng cách xóa 1, một số ký tự hoặc không xóa ký tự nào mà 
không làm thay đổi thứ tự cũa các ký tự còn lại trong chuỗi s
"""

from collections import defaultdict


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        if k == 25:
            return len(s)

        tmp = defaultdict()

        for idx, ele in enumerate(s):
            if ele not in tmp:
                tmp[ele] = 1

        return 0


sol = Solution()

s, k = "acfgbd", 2
print("ans: ", sol.longestIdealString(s, k))


# s, k = "abcd", 3
# print("ans: ", sol.longestIdealString(s, k))


# s, k = "acfgbdabcd", 0
# print("ans: ", sol.longestIdealString(s, k))  # 2


# s, k = "dacfgbdlkihabcd", 3
# print("ans: ", sol.longestIdealString(s, k))  # 10
