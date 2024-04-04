"""
1481. Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
 
Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

loại bó k số trong mảng để mảng chứa số lượng phần từ duy nhất là ít nhất 
"""

arr, k = [4, 3, 1, 1, 3, 3, 2], 3  # ans: 2

# arr, k = [2, 1, 1, 3, 3, 3], 3  # ans: 1

# arr, k = [4, 3, 1, 1, 3, 3, 2], 2  # 0

# arr, k = [2, 1, 1, 3, 3, 3], 3  # ans 1

# arr, k = [4,3,1,1,3,3,2], 3

# arr, k = [2, 4, 1, 8, 3, 5, 1, 3], 3

# arr, k = [1, 1, 2, 2, 3, 3], 3  # ans: 2

from collections import Counter

tmp = Counter(arr).copy()
count_arr = dict(sorted(tmp.items(), key=lambda item: item[1]))
count_k = k


print("sorted:  ", count_arr)


for item in list(count_arr.items()):

    value, count_val_arr = item

    if count_k >= count_val_arr:
        count_k -= count_val_arr
        del count_arr[value]
        break

    # if count <= 1 and count_k > 0:
    #     del count_arr[value]
    #     count_k -= 1
    # else:
    #     if count_k > 0:

    #         keys = [k for k, v in count_arr.items() if v == count_k]

    #         if len(keys) == 0:
    #             keys.append(value)

    #         print("check keys  ", count_arr, keys)

    #         for key in keys:
    #             if count_k > 0 and count > 1:
    #                 count_arr[key] -= 1

    #                 if count_arr[key] <= 1:
    #                     del count_arr[key]

    #                 count_k -= 1

    #         if count_k == 0:
    #             break
    print("con lai ", count_k, " lan xoa")
    print(count_arr)
print(count_arr)

print(len(count_arr.keys()))
