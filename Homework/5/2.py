n, a = map(int, input().split())
lst = []

for i in range(n):
    lst.append(tuple(map(int, input().split())))

lst.sort()

c = 0

for i in lst:
    if i[0] <= a:
        a += i[1]
        c += 1
    else:
        break

print(c)
