s = "Let's take LeetCode contest"  # return "s'teL ekat edoCteeL tsetnoc"


res = ""

for seq in s.split(" "):
    res = res + seq[::-1] + " "
print(res)


# ss=s.split()
# sss=[]
# for i in ss:
#     sss.append(i[::-1])
# return ' '.join(sss)
