"""
648. Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
"""

from typing import List
from collections import defaultdict


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        my_dict = defaultdict(list)

        for dct in dictionary:
            first_letter = dct[0]
            my_dict[first_letter].append(dct)
        print(my_dict)

        for word in sentence.split(" "):
            first_letter = word[0]
            if first_letter in my_dict:
                diction = my_dict[first_letter]

                

        return sentence


sol = Solution()
dictionary = ["cat", "cass", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(sol.replaceWords(dictionary, sentence))


# dictionary = ["a", "aa", "aaa", "aaaa"]
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# print(sol.replaceWords(dictionary, sentence))
