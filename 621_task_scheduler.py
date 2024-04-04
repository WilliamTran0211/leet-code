"""
621. Task Scheduler

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. 
Each cycle or interval allows the completion of one task. 
Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.


danh sách tasks và coldown n 
n là thời gian tasks quay lại làm việc
ví dụ N=2 và có 6 tasks AB
bất dầu từ task A 
đến task B là 1 cycle 
sau đó không làm gì là 1 cycle
sau đó tasks A là đảm bảo 2 tasks A cách nhau 2 cycle

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. 
The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle.
By the 4th cycle, you can do A again as 2 intervals have passed.

 
Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.


Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

"""

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # from collections import Counter

        # count_tasks = Counter(tasks)

        # res = []

        # for it in count_tasks.items():
        #     key, val = it

        #     if len(res) == 0:
        #         for i in range(val):
        #             res.append(key)
        #             res.extend(["*"] * n)
        #     else:
        #         count_fix = val
        #         count_n = n
        #         fix_flag = False
        #         for idx, str_val in enumerate(res):
        #             if str_val == "*":
        #                 if count_n - 1 != 0 and count_fix > 0:
        #                     res[idx] = key
        #                     count_n -= 1
        #                     fix_flag = True
        #                     count_fix -= 1
        #             elif str_val != key:
        #                 count_n = 2
        #                 fix_flag = False
        #                 continue

        #         if fix_flag is False and key not in res:
        #             for i in range(val):
        #                 res.append(key)
        #                 res.extend(["*"] * n)

        # stop_idx = -1

        # for idx in range(len(res) - 1, -1, -1):
        #     current = res[idx]

        #     next = res[idx - 1]

        #     if current != res[idx - 1]:
        #         stop_idx = idx
        #         break

        # print(res[0:stop_idx])
        return 0


sol = Solution()


tasks, n = ["A", "A", "A", "B", "B", "B"], 2
print("results: ", sol.leastInterval(tasks, n))


tasks, n = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2  # 12
print("results: ", sol.leastInterval(tasks, n))


tasks, n = ["A", "C", "A", "B", "D", "B"], 1  # 12
print("results: ", sol.leastInterval(tasks, n))


tasks, n = ["A", "A", "A", "B", "B", "B"], 3  # 10
print("results: ", sol.leastInterval(tasks, n))
