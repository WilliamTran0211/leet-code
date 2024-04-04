"""
452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. 
You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end. 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 


"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        balloon_nums = len(points)
        sort = sorted(points, key=lambda x: x[1])
        print(sort)
        shot_cnt = 0

        for idx, pt in enumerate(sort):
            start, end = pt[0], pt[1]
            if idx == 0:
                prev = end
            else:
                print("prev", prev, " current", start, end)
                if prev >= start and prev <= end:
                    shot_cnt += 1
                    print("can shoot ", shot_cnt)
                else:
                    prev = end
                    print("cannot shoot")
            print(sort)
        res = balloon_nums - shot_cnt

        print(balloon_nums, shot_cnt, res)

        return res


sol = Solution()

# points = [[10, 16], [2, 8], [1, 6], [7, 12]]
# print(sol.findMinArrowShots(points))

# points = [[2, 3], [2, 3]]  # 1
# print(sol.findMinArrowShots(points))

# points = [[0, 10], [20, 30], [40, 50], [60, 70]]
# print(sol.findMinArrowShots(points))

# points = [[-10, -5], [-7, 0], [2, 5], [7, 10]]
# print(sol.findMinArrowShots(points))

# # points = [[100, 200], [150, 250], [180, 220], [210, 230]]
# # print(sol.findMinArrowShots(points))

# points = [[-50, -40], [-30, -20], [-10, 0], [10, 20], [30, 40]]
# print(sol.findMinArrowShots(points))

# # points = [[500, 510], [520, 530], [540, 550], [560, 570], [580, 590]]
# # print(sol.findMinArrowShots(points))

# points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
# print(sol.findMinArrowShots(points))

points = [
    [3, 9],
    [7, 12],
    [3, 8],
    [6, 8],
    [9, 10],
    [2, 9],
    [0, 9],
    [3, 9],
    [0, 6],
    [2, 8],
]  # 2
print(sol.findMinArrowShots(points))
