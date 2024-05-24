"""
2812. Find the Safest Path in a Grid
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) 
is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Example 1:
Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

Example 2:
Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Example 3:
Input: grid = 
[   [0,0,0,1],
    [0,0,0,0],
    [0,0,0,0],
    [1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Kết quả trả về là khoảng cách manhattan nhỏ nhất của đoạn đường đi từ [0][0] đến vị trí [n-1][n-1]
Ví dụ example 3:
    Từ vị trí [0][0] đến vị trí có trộm là [0][3] và [3][0] thì khoảng cách manhattan là 3 theo công thức phía trên
    Từ vị trí [0][1] đến vị trí có trộm là [0][3] thì khoảng cách manhattan là 2.
    Vì vậy sau khi tính hết các vị trí mà con đường này đi qua thì chúng ta có đoạn đường như sau:
    [   [ * , * , 0 , 1],
        [ 0 , * , * , 0],
        [ 0 , 0 , * , *],
        [ 1 , 0 , 0 , *]]
    
        khoảng cách sau khi tính sẽ thành:

    [   [ 3 , 2 , 1 , 0],
        [ 2 , 3 , 2 , 1],
        [ 1 , 2 , 3 , 2],
        [ 0 , 1 , 2 , 3]]
        

    khoảng cách manhattan từ bất kì điểm nào trên đường là 2 hoặc 3 => kết quả là khoảng cách manhattan nhỏ nhất nên bằng 2
    
    Tuy nhiên do có nhiều đường đi nên phải chọn con đường có hệ số an toàn cao nhất trong tất cả các con đường 
    ví dụ: không thể chọn đường này:
    [   [ * , 0 , 0 , 1],
        [ * , 0 , 0 , 0],
        [(*), * , * , *],
        [ 1 , 0 , 0 , *]]
    
    *** Lý do là vì vị trí đường đi qua điểm [0][2] thì có khoảng cách manhattan là 1. 
    Do đó hệ số an toàn tối đa của con đường này là 1 so với con đường trên có hệ số an toàn cao hơn là 2 nên con đường trên là con đường chính xác

tóm lại: chọn con đường xa kẻ trộm nhất và trả về khoảng cách nhỏ nhất đến kẻ trộm từ bất kì điểm nào trên đường đó.   


cách tiếp cận từ vị trí 0 có khả năng dư thừa vì phải tìm tất cả các con đường đi đến 1 để tính vị trí của nó so với 1
vì vậy cách tiếp cận hợp lý hơn là đi từ vị trí 1 đề tính các khoảng cách
sau đó sử dụng max_heap (priority queue nhưng trả về kết quả lớn nhất khi pop) để lưu trữ đường đi sử dụng BFS

Vậy làm sao có thể tracking giá trị khoảng cách nhỏ nhất của đường đi.
khi lưu trữ trong max_heap với cấu trúc (khoảng cách, row, column)
 
khi sử dụng bfs sẽ duyệt qua tất cả các vị trí khả năng tiếp theo(là trên, dưới, trái, phải) 
sau đó push vào max_heap với cấu trúc trên. với từng vị trí "tiếp theo được push" vào max_heap, 
nếu vị trí tiếp theo có giá trị khoảng cách lớn hơn giá trị tối đa trong max_heap thì khi push vị trí mới vào 
ta sẽ thay thế giá trị khoảng cách bằng vị trí tối đa trong max_hea, vì vậy khi đến vị trí cuối cùng ta vẫn có thể tracking dc giá trị của khoảng cách nhỏ nhất của đường đi




(link: https://www.youtube.com/watch?v=-5mQcNiVWTs)
"""

from typing import List
from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # if grid[0][0] == 1 or grid[-1][-1] == 1:
        #     return 0

        def in_bound(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        def pre_compute():
            q = deque()
            min_dist = {}
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0

            while q:
                r, c, dist = q.popleft()
                nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

                for r2, c2 in nei:
                    if in_bound(r2, c2) and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist + 1])

            return min_dist

        min_dist = pre_compute()
        """
        Do python không có max_heap nên về cơ bản nó là min heap, 
        vì vậy thêm dấu âm vào giá trị khoảng cách, 
        khi đó khi pop trong heap nó lấy giá trị nhỏ nhất và
        bỏ giá trị âm đi nó sẽ thành giá trị lớn nhất trong heap
        """
        maxHeap = [(-min_dist[(0, 0)], 0, 0)]  # (distance, r, c)
        visit = set()

        visit.add((0, 0))
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist  # vì khi push vào giá trị âm nên cần bỏ âm đề lấy nguyên
            if (r, c) == (N - 1, N - 1):
                return dist
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for r2, c2 in nei:
                if in_bound(r2, c2) and (r2, c2) not in visit:
                    visit.add((r2, c2))
                    dist2 = min(dist, min_dist[(r2, c2)])
                    heapq.heappush(maxHeap, (-dist2, r2, c2))


sol = Solution()
grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
print("asn:", sol.maximumSafenessFactor(grid))
