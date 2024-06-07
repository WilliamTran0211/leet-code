"""
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
"""

from collections import Counter, defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count = defaultdict(int)

        # res = 0

        # for c in s:
        #     count[c] += 1
        #     if count[c] % 2 == 0:
        #         res += 2

        # for cnt in count.values():
        #     if cnt % 2:
        #         res += 1
        #         break

        # return res

        seen = set()
        res = 0
        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)

        return res + 1 if seen else res


sol = Solution()
print("ans: ", sol.longestPalindrome("Aaabcccddfffff"))

print("ans: ", sol.longestPalindrome("abccccdd"))

print("ans: ", sol.longestPalindrome("aabb"))

print("ans: ", sol.longestPalindrome("abcd"))

print("ans: ", sol.longestPalindrome("cc"))
