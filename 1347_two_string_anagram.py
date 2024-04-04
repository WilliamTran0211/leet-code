t = "aba"
s = "bab"

# t = "cabbba"
# s = "abbccc"

# s = "anagram"
# t = "mangaar"

# t = "practice"
# s = "leetcode"

s = "yplsbcvbuqjycfdgxdzfuvyxkceppqmtdmzfednkx"  # 16
t = "hjtiuoomfyeiencomvahzfsvqlqqumccburhadyua"


# sum((Counter(s) - Counter(t)).values()) #right and short answer


from collections import Counter

count_char_t = Counter(list(t))
count_char_s = Counter(list(s))

print("count_char_t ", count_char_t)
print("count_char_s ", count_char_s)

union_set = set(list(t)).union(set(list(s)))

test = {}
tt = []

for char in count_char_t:
    print("char ", char)
    print(count_char_t[char], count_char_s[char])

    if count_char_s[char] == 0:
        test[char] += 1
    else:
        if count_char_t[char] < count_char_s[char]:
            time = count_char_s[char] - count_char_t[char]
            test = count_char_s[char] - time
        

    print(test)
    print()


print(test)

# count_step = 0
# for char in set(list(t)).union(set(list(s))):
#     print("char  ", char)
#     print("val t =", count_char_t[char], " - s =", count_char_s[char])
#     tmp = abs(count_char_t[char] - count_char_s[char])
#     print("tmp  ", tmp)
#     if count_char_t[char] == count_char_s[char] and tmp != 0:
#         count_step += 1
#     elif count_char_s[char] != count_char_t[char]:
#         if count_char_s[char] == 0:
#             count_step += 1
#         else:
#             if tmp != count_char_s[char] and tmp != count_char_t[char]:
#                 count_step += tmp
#     print("count ", count_step)
#     print()

# if count_step == len(t) and check_set is True:
#     print(0)
# else:
#     print(count_step)
