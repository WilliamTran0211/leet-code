"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true


"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        tmp = {}
        tmp_t = {}
        for idx, ele in enumerate(s):
            tmp.setdefault(ele, set()).add(t[idx])
            tmp_t.setdefault(t[idx], set()).add(ele)
        for item in tmp.items():
            key_s, val_s = item
            if len(val_s) == 1:
                val = list(val_s)[0]

                val_t = tmp_t[val]
                if len(val_t) > 1:
                    return False
            else:
                return False
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:

        m_z = zip(s, t)

        print(tuple(m_z))

        return False


sol = Solution()

s = "egg"
t = "add"
print("ans:", sol.isIsomorphic(s, t))


s = "foo"
t = "bar"
print("ans:", sol.isIsomorphic(s, t))


s = "paper"
t = "title"
print("ans:", sol.isIsomorphic(s, t))


s = "BADC"
t = "BABA"
print("ans:", sol.isIsomorphic2(s, t))

s = "bbbaaaba"
t = "aaabbbba"
print("ans:", sol.isIsomorphic2(s, t))
