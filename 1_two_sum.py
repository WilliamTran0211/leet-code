nums = [2, 7, 8, 10, 9, 3]
target = 9

res = {}
for index, item in enumerate(nums):
    val = target - item
    if res.get(val, None) is not None:
        print([index, res[val]])
    else:
        res[item] = index
