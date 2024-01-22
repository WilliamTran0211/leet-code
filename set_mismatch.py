nums = [1, 2, 2, 4]
# nums = [1, 2, 3, 3, 5, 6, 7, 8, 9]
# nums = [2, 2]
nums = [1, 1]

tmp = []
dup_num = -1


for idx in range(len(nums)):
    if nums[idx] not in tmp:
        tmp.append(nums[idx])
    else:
        dup_num = nums[idx]

n_len = len(tmp)
sum_nums = sum(tmp)
total_sum = ((n_len + 1) * (n_len + 2)) / 2

print(sum_nums, total_sum)

print([dup_num, int(total_sum - sum_nums)])


# n = len(nums)
# a = sum(nums)
# b = sum(set(nums))
# s = n*(n+1)//2
# return [a-b, s-b]



