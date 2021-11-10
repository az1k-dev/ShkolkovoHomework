s, n, c = [int(i) for i in input().split()] + [0]
lst = sorted([int(input()) for i in range(n)])

for i in lst:
    s -= i
    if s >= 0:
        c += 1
    else:
        break

print(c)
