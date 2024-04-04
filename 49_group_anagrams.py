strs = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat",
]  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

res = []
tmp_dict = {}
for idx, s in enumerate(strs):
    tmp = list(s)

    rearrange_key = "".join(sorted(tmp))

    if rearrange_key not in tmp_dict.keys():
        tmp_dict[rearrange_key] = [s]
    else:
        tmp_dict[rearrange_key].append(s)

print(list(tmp_dict.values()))
