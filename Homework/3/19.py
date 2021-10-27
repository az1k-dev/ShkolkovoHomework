def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a

    a1 = []
    a2 = []

    v = a[n // 2]

    for i in range(n):
        if i == n // 2:
            continue
        if a[i] < v:
            a1.append(a[i])
        else:
            a2.append(a[i])

    return quick_sort(a1) + [v] + quick_sort(a2)


def main():
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    lst = quick_sort(lst)

    blue = []
    green = []
    red = []

    for i in range(n):
        s = lst[i]
        if s < 250:
            blue.append(s)
        elif s < 500:
            green.append(s)
        else:
            red.append(s)

    lst_b = []
    lst_p = []
    lst_a = []

    lst_b += blue[:5] + red[-2:]

    lst_p += green[:2]

    if len(blue) > 5:
        lst_p += blue[5:]

    if len(red) > 2:
        lst_a += red[:-2]

    print(sum(lst_b), sum(lst_p), sum(lst_a))


if __name__ == '__main__':
    main()
