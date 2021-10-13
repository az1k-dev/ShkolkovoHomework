def ms(a):
    n = len(a)

    if n == 1:
        return a

    return m(ms(a[:n//2]), ms(a[n//2:]))


def m(a, b):
    i, j = 0, 0

    ans = []

    for k in range(len(a) + len(b)):
        if i == len(a):
            ans.append(b[j])
            j += 1
        elif j == len(b):
            ans.append(a[i])
            i += 1
        elif a[i] > b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    return ans


if __name__ == '__main__':
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    lst = ms(lst)

    print(*lst)
