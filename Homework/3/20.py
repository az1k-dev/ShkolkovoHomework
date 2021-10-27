def f(a, h2, n):
    lst = [a, h2]

    for i in range(n - 2):
        s = 2 * (lst[-1] + 1) - lst[-2]
        if s < 0:
            return False
        lst.append(s)

    return lst[-1]


def bin_search(a, n):
    l = 0
    r = a + 1

    while r - l > 0.000001:
        s = (l + r) / 2

        if f(a, s, n) is False:
            l = s
        else:
            r = s

    return r


def main():
    n, a = map(int, input().split())

    h2 = bin_search(a, n)

    answer = f(a, h2, n)

    print(answer)


if __name__ == '__main__':
    main()
