"""
1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 
"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        cnt = Counter(words[0])

        for w in words:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])

        res = []

        for c in cnt:
            res.extend([c] * cnt[c])

        return res


sol = Solution()
words = ["bella", "label", "roller"]
print("ans: ", sol.commonChars(words))


words = [
    "acabcddd",
    "bcbdbcbd",
    "baddbadb",
    "cbdddcac",
    "aacbcccd",
    "ccccddda",
    "cababaab",
    "addcaccd",
]
print("ans ([]): ", sol.commonChars(words))
