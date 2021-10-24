def ms(a):
    n = len(a)

    if n == 1:
        return (0, a)
    else:
        return m(ms(a[n // 2:]), ms(a[:n // 2]))


def m(a, b):
    s = a[0] + b[0]
    a, b = a[1], b[1]
    i, j = 0, 0
    bn = len(b)
    ans = []

    def add_a():
        nonlocal i, s
        ans.append(a[i])
        i += 1
        s += bn - j

    def add_b():
        nonlocal j
        ans.append(b[j])
        j += 1

    for k in range(len(a) + len(b)):
        if i == len(a):
            add_b()
        elif j == len(b):
            add_a()
        elif a[i] < b[j]:
            add_a()
        else:
            add_b()

    return s, ans


def solve(a):
    n = len(a)

    for i in range(n):
        a[i] = (a[i], i)

    a = ms(a)

    return a[0]


if __name__ == '__main__':
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    answer = solve(lst)

    print(answer)
