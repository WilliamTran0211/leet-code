"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Tn = Tn+3 - Tn+2 - Tn+1

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537


"""


class Solution:
    def tribonacci(self, n: int) -> int:

        # brute force - time limit execution
        # def tri(n):
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 1
        #     return tri(n - 1) + tri(n - 2) + tri(n - 3)
        # return tri(n)

        # should have some conditions for the edge case suck as
        # when n<=2 then if n == 0 return 0 else return 1

        # useless spaces when it not needed can change to res = [0] *n +1
        res = [0] * 38

        res[0] = 0
        res[1] = 1
        res[2] = 1

        i = 3
        while i <= n:
            res[i] = res[i - 1] + res[i - 2] + res[i - 3]
            i += 1

        return res[n]


sol = Solution()
n = 4
print("ans: ", sol.tribonacci(n))


n = 25  # 1389537
print("ans: ", sol.tribonacci(n))


n = 31  # 53798080
print("ans: ", sol.tribonacci(n))
