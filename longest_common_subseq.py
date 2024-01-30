text1 = "abcde"
text2 = "ace"

# 1143 - longest common subsequence
"""
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".


Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"nano" a subsequence of "nematode knowledge"?
                         x  x      xx   => nano

explanation: https://www.youtube.com/watch?v=Ua0GhsJSlWM
https://ics.uci.edu/~eppstein/161/960229.html

"""

dp = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]

for i in range(len(text1) - 1, -1, -1):
    for j in range(len(text2) - 1, -1, -1):
        print(text1[i], text2[j])
        if text1[i] == text2[j]:
            dp[i][j] = 1 + dp[i + 1][j + 1]
        else:
            dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[0][0])
