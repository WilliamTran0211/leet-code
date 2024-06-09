"""
165. Compare Version Numbers
Medium
Topics
Companies
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".
Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2

"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        list_ver1 = version1.split(".")
        list_ver2 = version2.split(".")

        res = 0

        # diff_len = len(list_ver1) - len(list_ver2)
        # if diff_len > 0:
        #     list_ver2.extend(["0"] * diff_len)
        # elif diff_len < 0:
        #     list_ver1.extend(["0"] * abs(diff_len))

        # max_len = max(len(list_ver1), len(list_ver2))
        # list_ver1 += ["0"] * (max_len - len(list_ver1))
        # list_ver2 += ["0"] * (max_len - len(list_ver2))

        # diff_len = len(list_ver1) - len(list_ver2)
        # list_ver1.extend(["0"] * max(0, -diff_len))
        # list_ver2.extend(["0"] * max(0, diff_len))

        for idx in range(len(list_ver1)):
            if int(list_ver1[idx]) > int(list_ver2[idx]):
                res = 1
                break
            if int(list_ver1[idx]) < int(list_ver2[idx]):
                res = -1
                break
            else:
                continue

        return res


sol = Solution()
version1, version2 = "1.01", "1.001"
print("ans: ", sol.compareVersion(version1, version2))

version1, version2 = "1.0", "1.0.0"
print("ans: ", sol.compareVersion(version1, version2))

version1, version2 = "1.0.2", "1.0.0.1"
print("ans: ", sol.compareVersion(version1, version2))

# version1, version2 = "0.1", "1.1"
# print("ans: ", sol.compareVersion(version1, version2))

# version1, version2 = "1.2", "1.10"
# print("ans: ", sol.compareVersion(version1, version2))

# version1, version2 = (
#     "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000",
#     "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000",
# )
# print("ans: ", sol.compareVersion(version1, version2))  # ans: 0
