"""
506. Relative Ranks
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
"""

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        gold = "Gold Medal"
        silver = "Silver Medal"
        bronze = "Bronze Medal"

        tmp_sorted = sorted(score, reverse=True)
        res = {}
        for i in range(len(tmp_sorted)):
            if i == 0:
                res[tmp_sorted[i]] = gold
            if i == 1:
                res[tmp_sorted[i]] = silver
            if i == 2:
                res[tmp_sorted[i]] = bronze
            if i >= 3:
                res[tmp_sorted[i]] = str(i + 1)

        for i, sco in enumerate(score):
            score[i] = res[sco]
        return score


sol = Solution()
score = [10, 3, 8, 9, 4]
print("ans: ", sol.findRelativeRanks(score))


score = [5, 4, 3, 2, 1]
print("ans: ", sol.findRelativeRanks(score))
