"""
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        from collections import Counter

        count_s = Counter(s)

        print(count_s)

        return True


sol = Solution()

s = "()"
print("ans: ", sol.checkValidString(s))

s = "(*)"
print("ans: ", sol.checkValidString(s))

s = "(*))"
print("ans: ", sol.checkValidString(s))
