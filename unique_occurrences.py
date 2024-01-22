arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

from collections import Counter

count = Counter(arr)

# if len(counter) < len(count.keys()):
#     print(False)
# else:
#     print(True)

print(count)


my_dict = {}

for i in arr:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print(set(my_dict.values()))

print(len(set(my_dict.values())) == len(my_dict))
