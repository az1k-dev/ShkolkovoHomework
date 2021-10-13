def merge_sort(a, reverse=False, key=lambda s:s):
    n = len(a)

    if n == 1:
        return a

    a1 = a[:n // 2]
    a2 = a[n // 2:]

    sorted_a1 = merge_sort(a1, reverse=reverse, key=key)
    sorted_a2 = merge_sort(a2, reverse=reverse, key=key)

    sorted_a = merge(sorted_a1, sorted_a2, reverse=reverse, key=key)

    return sorted_a


def merge(a, b, reverse=False, key=lambda s:s):
    i, j = 0, 0

    n, s = len(a), len(b)

    merged = []

    def merge_a():
        nonlocal merged, a, i
        merged.append(a[i])
        i += 1

    def merge_b():
        nonlocal merged, b, j
        merged.append(b[j])
        j += 1

    for k in range(n + s):
        if i == n:
            merge_b()
        elif j == s:
            merge_a()
        elif key(a[i]) < key(b[j]):
            if reverse:
                merge_b()
            else:
                merge_a()
        else:
            if reverse:
                merge_a()
            else:
                merge_b()

    return merged


def count_even(lst):
    ans = 0

    for i in lst:
        if i % 2 == 0:
            ans += 1

    return ans


if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    lst = []

    for i in range(n):
        lst.append(list(map(int, input().split())))

    lst = merge_sort(lst, key=count_even)

    for i in lst:
        print(*i)
