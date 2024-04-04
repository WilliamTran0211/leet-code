s = "book"
s = "textbook"

s = "AbCdEfGh"

# s = "tkPAdxpMfJiltOerItiv"

from collections import Counter

vowels = ["a", "e", "i", "o", "u"]

h_length = int(len(s) / 2)

print(h_length)


s1, s2 = s[:h_length].lower(), s[h_length:].lower()

print(s1)
print(s2)

count_s1 = Counter(s1)
count_s2 = Counter(s2)

print(count_s1)
print(count_s2)

count1, count2 = 0, 0
for c in vowels:
    if c in count_s1:
        count1 += count_s1[c]
    if c in count_s2:
        count2 += count_s2[c]

print(count1, count2)

if count1 == count2:
    print("true")
else:
    print("false")
