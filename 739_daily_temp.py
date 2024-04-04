temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [30, 40, 50, 60]
temperatures = [30, 60, 90]
temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]  # [3,1,1,2,1,1,0,1,1,0]
"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0, 0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


# brute force
# res = []
# for i in range(len(temperatures)):
#     today = temperatures[i]
#     count = 0
#     for j in range(i + 1, len(temperatures)):
#         tomorrow = temperatures[j]
#         if tomorrow > today:
#             count += 1
#             break
#         else:
#             if j < len(temperatures) - 1:
#                 count += 1
#             else:
#                 count = 0
#     res.append(count)

# print(res)

res = []
for idx, temperature in enumerate(temperatures):

