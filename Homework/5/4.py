n = int(input())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst_p = []
lst_t = []

for i in range(n):
    lst_p.append((i, lst1[i]))

for i in range(n):
    lst_t.append((i, lst2[i]))

lst_t.sort(key=lambda s: s[1])
lst_p.sort(key=lambda s: s[1], reverse=True)

lst = []

for i in range(n):
    lst.append((lst_p[i][0], lst_t[i][0]))

lst.sort(key=lambda s: s[0])

lst_answer = []

for i in range(n):
    lst_answer.append(lst[i][1] + 1)

print(*lst_answer)
