def quick_sort(a, l=0, r=None):
    if r is None:
        r = len(a) - 1

    if l == r:
        return

    s = part(a, l, r)
    print(a, l, '-', r, '->', s)
    quick_sort(a, l, s)
    quick_sort(a, s + 1, r)


def part(a, l, r):
    s = (l + r) // 2
    v = a[s]

    i, j = l, r

    while i < j:
        while a[i] < v:
            i += 1
        while a[j] > v:
            j -= 1

        if j <= i:
            break

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return j


if __name__ == '__main__':
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    quick_sort(lst)

    print(lst)
