def merge_sort(a, lvl=0):
    print('|   ' * lvl + "Not sorted: " + str(a))
    n = len(a)

    if n == 1:
        ans = a
    else:
        ans = merge(merge_sort(a[:n // 2], lvl + 1), merge_sort(a[n // 2:], lvl + 1))

    print('|   ' * lvl + "Sorted: " + str(ans))
    print('|   ' * lvl)

    return ans


def merge(a, b):
    ans = []

    i, j = 0, 0

    while i < len(a) or j < len(b):
        if i == len(a):
            ans.append(b[j])
            j += 1
        elif j == len(b):
            ans.append(a[i])
            i += 1
        elif a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    return ans


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))

    merge_sort(lst)
