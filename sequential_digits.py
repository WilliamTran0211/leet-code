low = 178546104
high = 812704742

"""
An integer has sequential digits if and 
only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

[

       12,       23,       34,        45,

       56,       67,       78,        89,

      123,      234,      345,       456,

      567,      678,      789,      1234,

     2345,     3456,     4567,      5678,

     6789,    12345,    23456,     34567,

    45678,    56789,   123456,    234567,

   345678,   456789,  1234567,   2345678,

  3456789, 12345678, 23456789, 123456789

]

"""

# regen_lst = [
#     12,
#     23,
#     34,
#     45,
#     56,
#     67,
#     78,
#     89,
#     123,
#     234,
#     345,
#     456,
#     567,
#     678,
#     789,
#     1234,
#     2345,
#     3456,
#     4567,
#     5678,
#     6789,
#     12345,
#     23456,
#     34567,
#     45678,
#     56789,
#     123456,
#     234567,
#     345678,
#     456789,
#     1234567,
#     2345678,
#     3456789,
#     12345678,
#     23456789,
#     123456789,
# ]


# top_idx = -1
# bottom_idx = -1

# flag_1 = False
# flag_2 = False

# for i in range(len(regen_lst)):
#     if regen_lst[i] > low and flag_1 == False:
#         top_idx = i
#         flag_1 = True

#     if regen_lst[len(regen_lst) - 1 - i] <= high and flag_2 == False:
#         bottom_idx = len(regen_lst) - i
#         flag_2 = True

#     if flag_1 == True and flag_2 == True:
#         break

# if flag_1 != flag_2:
#     return []

# print(regen_lst[top_idx:bottom_idx])


digits = "123456789"
result = []
len_low = len(str(low))
len_high = len(str(high))
for i in range(len_low, len_high+1):
    for j in range(0, 10-i):
        num = int(digits[j: j+i])
        if num >= low and num <= high:
            result.append(num)
print(result)