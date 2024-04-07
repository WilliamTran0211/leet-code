"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.

Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        key = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        dou_key = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        lst_s = list(s)

        count = 0

        for i in range(len(lst_s)):
            char = lst_s[i]
            next_char = " "
            if i < len(lst_s) - 1:
                next_char = lst_s[i + 1]
            comp = char + next_char
            if char in key.keys():
                if comp in dou_key.keys():
                    count += dou_key[comp]
                    lst_s[i] = " "
                    lst_s[i + 1] = " "
                else:
                    count += key[char]
                    lst_s[i] = " "
            elif i + 1 == len(lst_s) - 1:
                count += key[next_char]
                lst_s[i + 1] = " "


        return count


sol = Solution()

s = "III"
print("ans: ", sol.romanToInt(s))

s = "LVIII"
print("ans: ", sol.romanToInt(s))

s = "MCMXCIV"
print("ans: ", sol.romanToInt(s))

s = "MMXXIV"
print("ans: ", sol.romanToInt(s))

s = "XXXII"
print("ans: ", sol.romanToInt(s))
