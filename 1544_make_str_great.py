"""
1544. Make The String Great

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them.
 You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, 
both will result "leEeetcode" to be reduced to "leetcode".


Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"
 
"""


class Solution:
    def makeGood(self, s: str) -> str:
        lst_str = list(s)

        res = []

        while len(lst_str) > 0:
            pop_str = lst_str.pop()

            if len(res) == 0:
                res.append(pop_str)
            else:
                last_in_stack = res[-1]
                if (
                    last_in_stack.lower() == pop_str.lower()
                    and last_in_stack != pop_str
                ):
                    res.pop()
                else:
                    res.append(pop_str)

        return "".join(res[::-1])


sol = Solution()


s = "leEeetcode"  # leetcode
print("ans: ", sol.makeGood(s))

s = "abBAcC"  # ""
print("ans: ", sol.makeGood(s))

s = "s"  # "s"
print("ans: ", sol.makeGood(s))

s = "nThYCFZCwfFzjNTsyYuUyYqvVStnxXfFnNdSsBQqPJNnwWnDdZfQqqFWwQqFXxIWXxchzfcGgDdjyHtziInNMEhHqQkKkwyQqgG"  # "nThYCFZCwzjNTsqStndBPJnZfqFFIWchzfcjyHtzMEkwy"
ans = "nThYCFZCwzjNTsqStndBPJnZfqFFIWchzfcjyHtzMEkwy"
print("ans: ", sol.makeGood(s), " check ans: ", sol.makeGood(s) == ans)
