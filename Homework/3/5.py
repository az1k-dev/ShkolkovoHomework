def merge_sort(a):
    n = len(a)

    if n == 1:
        return a
    else:
        return merge(merge_sort(a[n // 2:]), merge_sort(a[:n // 2]))


def merge(a, b):
    i, j = 0, 0

    ans = []

    for _ in range(len(a) + len(b)):
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


def solve(lst):
    n = len(lst)

    k = n // 2

    lst = merge_sort(lst)

    answer = sum(lst[k:])

    return answer


if __name__ == '__main__':
    n = int(input())

    lst = list(map(int, input().split()))

    print(solve(lst))
