nums = [1, 2, 3, 1]
# nums = [2, 1, 1, 2]  # 4
nums = [40, 2, 4, 10, 1, 5]  # 55 = 40 + 10 + 5
# 198. House Robber
# 2 nhà ko dc liền kề nhau nên có thể cách 2 nhà


rob1, rob2 = 0, 0

# [rob1, rob2, n, n+1,....]
for n in nums:
    tmp = max(n + rob1, rob2)
    rob1 = rob2
    rob2 = tmp

print(rob2)


# another solution
n = len(nums)
if n == 1:
    print(nums[0])
p = [0] * (n + 1)
print(p)
p[1] = nums[0]
print(p)

for i in range(1, n):
    p[i + 1] = max(p[i - 1] + nums[i], p[i])
    print(p)


print(p)
print(p[n])
