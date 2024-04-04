s = "anagramr"
t = "nagarams"


from collections import Counter

ss = Counter(s)
tt = Counter(t)

print(ss == tt)


if len(s) != len(t):
    print(False)
for i in set(s):
    if s.count(i) != t.count(i):
        print(False)
print(True)
