"""
787. Cheapest Flights Within K Stops
Medium
Topics
Companies
There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [from i, to i, price i] 
indicates that there is a flight from city from i to city toi with cost price i.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.


"""

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        
        

        return 0


sol = Solution()


# Output: 700
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1


# Output: 200
n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1


print(sol.findCheapestPrice(n, flights, src, dst, k))
