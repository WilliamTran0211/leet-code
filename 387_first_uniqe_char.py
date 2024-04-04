s = "loveleetcodv"


for idx, char in enumerate(s):
    if s.count(char) == 1:
        print(idx)
        break

print(-1)

# for i in s:
#     if s.rindex(i) == s.index(i):  #rindex() find the last character i occur in the string 
#         return s.index(i)    #index() find the first character i occur in the string
# return -1


