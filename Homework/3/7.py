def merge_sort(a, reverse=False):
    n = len(a)

    if n == 1:
        return a
    else:
        return merge(merge_sort(a[:n // 2], reverse=reverse),
                     merge_sort(a[n // 2:], reverse=reverse), reverse=reverse)


def merge(a, b, reverse=False):
    i, j = 0, 0

    ans = []

    for k in range(len(a) + len(b)):
        if i == len(a):
            ans.append(b[j])
            j += 1
        elif j == len(b):
            ans.append(a[i])
            i += 1
        elif a[i] < b[j]:
            if reverse:
                ans.append(b[j])
                j += 1
            else:
                ans.append(a[i])
                i += 1
        else:
            if reverse:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

    return ans


def solve(lst):
    n = len(lst)

    answer = 0

    max_s = lst[0] + 3

    for i in range(n):
        if lst[i] + 3 <= max_s:
            max_s = lst[i]
            answer += 1

    return answer


if __name__ == '__main__':
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    lst = merge_sort(lst, reverse=True)

    answer = solve(lst)

    print(answer)
