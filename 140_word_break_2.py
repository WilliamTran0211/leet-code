"""
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def backtrack(i):

            if i == len(s):
                res.append(" ".join(cur))
                return

            for j in range(i, len(s)):
                w = s[i : j + 1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j + 1)
                    cur.pop()

        cur = []
        res = []
        backtrack(0)
        return res


sol = Solution()

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print("ans: ", sol.wordBreak(s, wordDict))
