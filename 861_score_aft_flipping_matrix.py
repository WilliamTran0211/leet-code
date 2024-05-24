"""
861. Score After Flipping Matrix
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column 
(i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, 
and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).


Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:
Input: grid = [[0]]
Output: 1

a bit str with more 1 is bigger tha other
There are only two rules that you need to know in this problem. 
If the first number in the row is 0, flip the row. 
If the count of 0 in the col is greater than the count of 1, flip the col.
 
"""

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for idx_r, r in enumerate(grid):
            if r[0] == 0:
                for idx in range(len(r)):
                    grid[idx_r][idx] = 1 if r[idx] == 0 else 0

        for idx_c in range(len(grid[0])):
            col = [sub[idx_c] for sub in grid]

            if col.count(0) > col.count(1):
                for idx in range(len(col)):
                    grid[idx][idx_c] = 1 if col[idx] == 0 else 0
        res = 0
        for r in grid:
            res += int("".join(str(i) for i in r), 2)

        return res


sol = Solution()
grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
print("ans: ", sol.matrixScore(grid))


grid = [
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
]
print("ans: ", sol.matrixScore(grid))  # 15744
