"""
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

 

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [list(s)]

        res = []

        substring = []

        def dfs(i):
            if i >= len(s):
                res.append(substring.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    substring.append(s[i : j + 1])
                    dfs(j + 1)
                    substring.pop()

        dfs(0)

        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


sol = Solution()

s = "aab"
output = [["a", "a", "b"], ["aa", "b"]]
ans = sol.partition(s)
print(ans)
print("ans: ", output == ans)

s = "abcaa"
output = [["a", "b", "c", "a", "a"], ["a", "b", "c", "aa"]]
ans = sol.partition(s)
print("ans: ", output == ans)

s = "abbab"
output = [
    ["a", "b", "b", "a", "b"],
    ["a", "b", "bab"],
    ["a", "bb", "a", "b"],
    ["abba", "b"],
]
ans = sol.partition(s)
print("ans: ", output == ans)
