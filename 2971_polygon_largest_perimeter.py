"""
2971. Find Polygon With the Largest Perimeter


You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak 
where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak,
 then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.

 

Example 1:
Input: nums = [5,5,5]
Output: 15
Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.


Example 2:
Input: nums = [1,12,1,2,5,50,3]
Output: 12
Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. 
The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side 
because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12.


Example 3:
Input: nums = [5,5,50]
Output: -1
Explanation: There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.
 
"""

nums = [1, 12, 1, 2, 5, 50, 3]  # ans = 12
nums = [5, 5, 5]

nums = [1, 5, 1, 5]


sorted_list = sorted(nums, reverse=True)

print("sorted: ", sorted_list)

can_be_polygon = []
biggest_side = -1

list_len = len(sorted_list)
temp_list = sorted_list
for idx, side in enumerate(sorted_list):
    temp_list = sorted_list[idx + 1 :]
    if len(temp_list) >= 2:
        biggest_side = side
        can_be_polygon.append((biggest_side, sum(temp_list)))
    else:
        break

print(can_be_polygon)

max_peri = -1

for biggest_side, sum_other_sides in can_be_polygon:
    if biggest_side < sum_other_sides and max_peri < sum_other_sides:
        max_peri = sum_other_sides + biggest_side


print(max_peri)


# other way

new_list = sorted(nums)
total_sum = sum(sorted_list)

for i in range(list_len - 1, 1, -1):
    total_sum -= new_list[i]
    if total_sum > new_list[i]:
        print(total_sum + new_list[i])
        exit()
print(-1)