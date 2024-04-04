"""
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


"""

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # minimum_believer = n - 1
        # believers = set()
        # can_be_judge = set()

        # for relation in trust:
        #     a, b = relation
        #     believers.add(a)
        #     can_be_judge.add(b)

        # res = can_be_judge - believers

        # print(minimum_believer, believers, can_be_judge, res)

        # if len(res) == 0 or len(believers) < minimum_believer:
        #     return -1
        # else:
        #     return res.pop()

        # at_least_believer = n - 1
        # can_be_judge = dict()
        # believers = set()
        # for tr in trust:
        #     believers.add(tr[0])
        #     judge_candidate = tr[-1]
        #     can_be_judge[judge_candidate] = can_be_judge.get(judge_candidate, 0) + 1

        # judge_candidate = set(can_be_judge.keys())
        # res = judge_candidate - believers

        # print(res, judge_candidate, believers, at_least_believer)

        # if len(res) == 0 or len(believers) < at_least_believer:
        #     return -1
        # return res.pop()

        if n == 1:
            return 1

        minimum_believer = n - 1
        judge_candidates = dict()
        believers = set()

        for relation in trust:
            believer = relation[0]
            can_be_judge = relation[1]

            judge_candidates[can_be_judge] = judge_candidates.get(can_be_judge, 0) + 1
            believers.add(believer)

        res = (judge_candidates.keys()) - believers

        if len(res) > 0:
            candidate = res.pop()
            believer_cnt = judge_candidates[candidate]
            if believer_cnt == minimum_believer:
                return candidate

        return -1


sol = Solution()


trust, n = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 4  # 3

# trust, n = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3], [3, 4]], 4  # -1


trust, n = [[1, 3], [2, 3], [3, 1]], 3  # -1

trust, n = [[1, 2]], 2  # 2

trust, n = [[1, 3], [2, 3]], 4  # -1

trust, n = [[1, 2], [2, 3]], 3  # -1

trust, n = [], 1

print(sol.findJudge(n, trust))
