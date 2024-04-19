"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
 The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
 One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0

        vertical_len = len(grid)
        horizon_len = len(grid[0])

        for i in range(vertical_len):
            for j in range(horizon_len):
                current = grid[i][j]

                print(current)
                # if current == 1:
                #     print("found land")
            print()

        return 1


sol = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print("ans: ", sol.islandPerimeter(grid))
