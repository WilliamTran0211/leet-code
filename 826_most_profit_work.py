"""
826. Most Profit Assigning Work
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

Example 2:
Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0


worker thứ i chỉ có thể làm công việc có độ khó tối đa ở worker thứ i. 
Ví dụ trong example 1 thì worker thứ 0 có khả năng là 4 chỉ có thể làm công việc có độ khó <= 4 trong arr difficulty 
nên trong ví dụ thứ 2 worker có khả năng là 40,25,25 mà arr difficulty đều lớn hơn nên profit là 0

1 worker chỉ có thể làm 1 job nên nếu làm xong phải pop ra khỏi mảng, nếu ko làm dc cũng pop ra khỏi mảng. 
Nhưng 1 job trong diffculty có thể làm dc nhiều lần. 
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # brute force: correct but time limit exceeded
        # res = 0

        # map_profit_diff = defaultdict(int)

        # for prof, diff in zip(profit, difficulty):
        #     map_profit_diff[diff] = max(prof, map_profit_diff[diff])

        # current_profit = 0
        # for w in worker:
        #     for diff in map_profit_diff.keys():
        #         if diff <= w:
        #             current_profit = max(current_profit, map_profit_diff[diff])
        #     res += current_profit
        #     current_profit = 0

        # return res

        res = 0
        jobs = zip(difficulty, profit)
        sort_jobs = sorted(jobs)
        worker.sort()
        i = 0
        current_val = 0
        for w in worker:
            while i < len(difficulty) and w >= sort_jobs[i][0]:
                current_val = max(current_val, sort_jobs[i][1])
                i += 1
            res += current_val

        return res


sol = Solution()
difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
print("asn: ", sol.maxProfitAssignment(difficulty, profit, worker))


diff = [2, 17, 19, 20, 24, 29, 33, 43, 50, 51, 57, 67, 70, 72, 73, 75, 80, 82, 87, 90]
profit = [6, 7, 10, 17, 18, 29, 30, 31, 34, 39, 40, 42, 48, 54, 57, 78, 78, 78, 83, 88]
worker = [12, 9, 11, 41, 11, 87, 48, 6, 48, 93, 76, 73, 7, 50, 55, 97, 47, 33, 46, 10]
print("asn (expected: 693) ", sol.maxProfitAssignment(diff, profit, worker))


# difficulty = [
#     66,
#     1,
#     28,
#     73,
#     53,
#     35,
#     45,
#     60,
#     100,
#     44,
#     59,
#     94,
#     27,
#     88,
#     7,
#     18,
#     83,
#     18,
#     72,
#     63,
# ]
# profit = [
#     66,
#     20,
#     84,
#     81,
#     56,
#     40,
#     37,
#     82,
#     53,
#     45,
#     43,
#     96,
#     67,
#     27,
#     12,
#     54,
#     98,
#     19,
#     47,
#     77,
# ]
# worker = [
#     61,
#     33,
#     68,
#     38,
#     63,
#     45,
#     1,
#     10,
#     53,
#     23,
#     66,
#     70,
#     14,
#     51,
#     94,
#     18,
#     28,
#     78,
#     100,
#     16,
# ]
# print("asn (expected: 1392) ", sol.maxProfitAssignment(difficulty, profit, worker))
