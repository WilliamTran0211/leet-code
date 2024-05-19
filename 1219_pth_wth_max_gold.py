"""
1219. Path with Maximum Gold
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if (
                min(r, c) < 0
                or r == row
                or c == col
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0

            visit.add((r, c))
            res = 0

            res = grid[r][c]

            neigh = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for r2, c2 in neigh:
                res = max(res, grid[r][c] + dfs(r2, c2, visit))

            visit.remove((r, c))

            return res

        res = 0

        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r, c, set()))

        return res


sol = Solution()
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print("ans: ", sol.getMaximumGold(grid))


grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print("ans: ", sol.getMaximumGold(grid))
