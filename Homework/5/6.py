n = int(input())

card1 = list(map(lambda s: int(s), list(input())))
card2 = list(map(lambda s: int(s), list(input())))

card1.sort()
card2.sort()

lst1 = [0] * 10
lst2 = [0] * 10
lst11 = [0] * 10
lst21 = [0] * 10

for i in range(n):
    lst1[card1[i]] += 1
    lst2[card2[i]] += 1
    lst11[card1[i]] += 1
    lst21[card2[i]] += 1


def solve1(lst1, lst2):
    for i in range(9, -1, -1):
        for j in range(i, -1, -1):
            lst2[i] -= lst1[j]
            lst1[j] = 0
            if lst2[i] < 0:
                lst1[j] = -lst2[i]
                lst2[i] = 0
                break

    return sum(lst1)


def solve2(lst1, lst2, n):
    for i in range(9, -1, -1):
        for j in range(i - 1, -1, -1):
            lst2[i] -= lst1[j]
            lst1[j] = 0
            if lst2[i] < 0:
                lst1[j] = -lst2[i]
                lst2[i] = 0
                break

    return n - sum(lst1)


print(solve1(lst1, lst2))
print(solve2(lst11, lst21, n))
