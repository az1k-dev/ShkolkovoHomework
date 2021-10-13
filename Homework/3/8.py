def ms(a, r=False, f=lambda s: s):
    n = len(a)

    if n == 1:
        return a
    else:
        return m(ms(a[n // 2:], r=r, f=f), ms(a[:n // 2], r=r, f=f), r=r, f=f)


def m(a, b, r, f):
    i, j = 0, 0

    ans = []

    def f_b():
        nonlocal ans, b, j
        ans.append(b[j])
        j += 1

    def f_a():
        nonlocal ans, a, i
        ans.append(a[i])
        i += 1

    for k in range(len(a) + len(b)):
        if i == len(a):
            f_b()
        elif j == len(b):
            f_a()
        elif f(a[i]) < f(b[j]):
            if r:
                f_b()
            else:
                f_a()
        else:
            if r:
                f_a()
            else:
                f_b()

    return ans


if __name__ == '__main__':
    n = int(input())

    lst = []

    for i in range(n):
        info = input().split()

        name = info[0] + ' ' + info[1]
        points = sum(map(int, info[2:]))

        lst.append((name, points))

    lst = ms(lst, r=True, f=lambda s: s[1])

    for i in lst:
        print(i[0])
