# Basically Its a Fibonacci problem but start at 1
n = 3

f1 = 1
f2 = 2
if n == 1:
    print(1)
if n == 2:
    print(2)
else:
    f = 0
    for i in range(2, n):
        f = f1 + f2

        f1 = f2
        f2 = f

    print(f)
