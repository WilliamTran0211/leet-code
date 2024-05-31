"""
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
"""

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)

        # out of time O(n^4)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         for k in range(j, n):
        #             a, b = 0, 0

        #             for idx in range(i, j):
        #                 a ^= arr[idx]

        #             for idx in range(j, k + 1):
        #                 b ^= arr[idx]

        #             if a == b:
        #                 res += 1

        # O(n^3)
        # for i in range(n - 1):
        #     a = 0
        #     for j in range(i + 1, n):
        #         a ^= arr[j - 1]
        #         b = 0
        #         for k in range(j, n):
        #             b ^= arr[k]
        #             if a == b:
        #                 res += 1

        # nếu a = b thì khi XOR a và b sẽ có kết quả là 0
        # O(n^2)

        for i in range(n - 1):
            cur_xor = arr[i]
            for k in range(i + 1, n):
                cur_xor ^= arr[k]
                if cur_xor == 0:
                    res += k - i

        return res


sol = Solution()
print("ans: ", sol.countTriplets([2, 3, 1, 6, 7]))
