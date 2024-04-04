"""

791. Custom Sort String

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.


Example 1:

Input:  order = "cba", s = "abcd" 

Output:  "cbad" 

Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in order, 
it can be at any position in the returned string. 
"dcba", "cdba", "cbda" are also valid outputs.

Example 2:

Input:  order = "bcafg", s = "abcd" 

Output:  "bcad" 

Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. 
The character "d" in s does not appear in order, so its position is flexible.

Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". 
"d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule.
 Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
 
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # list_s = list(s)

        # pattern = [char for char in order if char in list_s]

        # left_over_chars = [char for char in s if char not in pattern]

        # print(pattern, left_over_chars)

        # str_left_over = "".join(left_over_chars)

        # replace_str = s.replace(str_left_over, "")

        # from collections import Counter

        # cnt = Counter(replace_str)

        # pattern_str = []
        # for char in pattern:
        #     number_of_char = cnt.get(char, 0)
        #     tmp_str = "".join([char] * number_of_char)
        #     pattern_str.append(tmp_str)

        # return "{s}{f}".format(s="".join(pattern_str), f=str_left_over)

        list_order_revers = list(order[::-1])
        tmp_str = s

        for char in list_order_revers:
            if char not in tmp_str:
                continue
            else:
                tmp_str = tmp_str.split(char)
                len_str = len(tmp_str)
                tmp_arr = [char] * (len_str - 1)
                tmp_str = tmp_arr + tmp_str
                tmp_str = "".join(tmp_str)

        return tmp_str


order = "cbafecvx"
# s = "fghiklmnoaabf"

s = "qwbkipotr"

sol = Solution()

print(sol.customSortString(order, s))
