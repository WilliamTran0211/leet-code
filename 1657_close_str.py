# word1 = "abbzzca"
# word2 = "babzzcz"
# word1 = "cabbba"
# word2 = "abbccc"

word1 = "uau"
word2 = "xsx"

set_w1 = set(word1)
set_w2 = set(word2)

if len(word1) != len(word2) or set_w1 != set_w2:
    print(False)

w1 = {}
w2 = {}

for w in word1:
    w1[w] = w1.get(w, 0) + 1

for w in word2:
    w2[w] = w2.get(w, 0) + 1

lis1 = sorted(w1.values())
lis2 = sorted(w2.values())

for idx, itm in enumerate(lis1):
    if itm == lis2[idx]:
        continue
    else:
        print(False)
print(True)
