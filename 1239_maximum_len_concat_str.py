arr = ["cha", "r", "act", "ers"]
# arr = ["abcdefghijklmnopqrstuvwxyz"]

# problem - 1239 : maximum length of aa concatenated string with unique characters

"""
"""


from collections import Counter

charSet = set()


def overlap(charset, s):
    c = Counter(charset) + Counter(s)

    return max(c.values()) > 1


def backtrack(i):
    if i == len(arr):
        return len(charSet)

    res = 0
    if not overlap(charSet, arr[i]):
        for c in arr[i]:
            charSet.add(c)
        res = backtrack(i + 1)
        for c in arr[i]:
            charSet.remove(c)

    return max(res, backtrack(i+1))


print(backtrack(0))