stones = [0, 1, 3, 5, 6, 8, 12, 17]  # true
# 403. Frog jump
"""
A frog is crossing a river. The river is divided into some number of units, 
and at each unit, there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, 
determine if the frog can cross the river by landing on the last stone. 
Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, 
its next jump must be either k - 1, k, or k + 1 units.
 The frog can only jump in the forward direction.

 

Example 1:
            no.  1 2 3 4 5 6  7  8
Input: stones = [0,1,3,5,6,8, 12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 
1 unit  to the 2nd stone, 
2 units to the 3rd stone, 
2 units to the 4th stone, 
3 units to the 6th stone, 
4 units to the 7th stone, 
5 units to the 8th stone.
"""
units = stones

stones_len = len(stones)

jum

for idx, unit in enumerate(units):
    if idx == 0:
        continue
    else:
        print(idx, unit)
