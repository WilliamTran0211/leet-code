from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)

        print(counts)

        convert_dict = {}

        for key, value in counts.items():
            convert_dict.setdefault(value, []).append(key)

        max_freq = max(convert_dict.keys())

        print(max(counts.values()))
        return len(convert_dict[max_freq]) * max_freq


sol = Solution()


nums = [1, 2, 2, 3, 1, 4, 1, 2, 3, 3]


print(sol.maxFrequencyElements(nums))
