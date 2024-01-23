arr = [3, 1, 2, 4]  # Answer = 17
# arr = [11, 81, 94, 43, 3]  # Answer = 444
arr = [2, 9, 7, 8, 3, 6, 1]  # Answer = 94
arr = [2, 9, 7, 8, 3, 6, 1, 5]  # Answer = 106


"""
sub array of array is ranges over every contiguous sub array
Sub arrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
"""

# arr_len = len(arr)
# total_sub_arr = ((arr_len + 1) * 4) // 2    # here is the total number of sub arrays can create from the array

"""
Monotonic stack: là môt cấu trúc dữ liệu lưu trữ một cách đơn điệu các phần tử theo cấu trúc tăng đần
hoặc giảm dần. Mang tất cả tính chất của một stack đơn thuần.

thường dc xử dụng trong các bài toán tìm phần tử nhỏ nhất/lớn nhất tiếp theo. 
Do khi một phần tử được pop khỏi stack nó sẽ không được xử dụng lại. 
Monotonic stack duy trì tính đơn điệu khi pop các phần tử khi 1 phần tử mới được đầy vào stack.  

phân tích => đếm số lần 1 số trong mảng trở thành số nhỏ nhất trong mảng con đó.

"""

MOD = 10**9 + 7
res = 0
stack = []
# arr = [float("-inf")] + arr + [float("-inf")] #add this line can remove codes from 59 -> 63 because can handle the edge case and stack empty

# sums=[0 for a in arr]
# print(sums)

# for i,a in enumerate(arr):
#     while stack and arr[stack[-1]]>a:
#         stack.pop()
#     j = stack[-1] if stack else -1
#     sums[i] = sums[j]+(i-j)*a
#     stack.append(i)
# print(sum(sums)%(10**9+7))

stack = []
for idx, ele in enumerate(arr):
    while stack and ele < stack[-1][1]:
        # stack[-1][1] is [-1] getting last element of an array, [1] is getting the second value of tuples
        j, m = stack.pop()
        print("pop", j, m)
        left = j - stack[-1][0] if stack else j + 1
        right = idx - j
        print("left ", left, "right   ", right)
        res = res + m * left * right
        print(res)
    stack.append((idx, ele))


print(stack, res)

for i in range(len(stack)):
    j, n = stack[i]
    left = j - stack[i - 1][0] if i > 0 else j + 1
    right = len(arr) - j
    res = res + n * left * right

print("final ans: ", res % MOD)
