def main():
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(list(map(int, input().split())))

    lst = merge_sort(lst, key=lambda s: s[1])

    for i in lst:
        print(*i)


def merge_sort(a, key=lambda s: s, reverse=False):
    n = len(a)

    if n == 1:
        return a

    sorted_b = merge_sort(a[:n // 2], key=key, reverse=reverse)
    sorted_c = merge_sort(a[n // 2:], key=key, reverse=reverse)

    sorted_a = merge(sorted_b, sorted_c, key=key, reverse=reverse)

    return sorted_a


def merge(a, b, key, reverse):
    i, j = 0, 0
    answer = []

    def add_a():
        nonlocal i
        answer.append(a[i])
        i += 1

    def add_b():
        nonlocal j
        answer.append(b[j])
        j += 1

    for k in range(len(a) + len(b)):
        if i == len(a):
            add_b()
        elif j == len(b):
            add_a()
        elif key(a[i]) > key(b[j]):
            if not reverse:
                add_a()
            else:
                add_b()
        else:
            if not reverse:
                add_b()
            else:
                add_a()

    return answer


if __name__ == '__main__':
    main()
