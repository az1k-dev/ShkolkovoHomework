def main():
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    heap_sort(lst)

    new_lst = []

    for i in range(n):
        new_lst.append(lst[-i - 1])

    lst = new_lst

    s = n // 3

    lst1 = lst[:s]
    lst2 = lst[s:]

    print(*lst1)
    print(*lst2)


def heapify(a, i=0, finish=None, start=False):
    if finish is None:
        finish = len(a)

    i1 = i * 2 + 1
    i2 = i * 2 + 2

    if not i1 < finish:
        return

    if not i2 < finish:
        if a[i1] > a[i]:
            a[i], a[i1] = a[i1], a[i]
        return

    if start:
        heapify(a, i1, finish, start)
        heapify(a, i2, finish, start)

    if a[i1] > a[i] or a[i2] > a[i]:
        if a[i1] > a[i2]:
            a[i], a[i1] = a[i1], a[i]
            heapify(a, i1, finish)
        else:
            a[i], a[i2] = a[i2], a[i]
            heapify(a, i2, finish)


def heap_sort(a):
    n = len(a)

    heapify(a, start=True)

    for i in range(n):
        j = n - i

        heapify(a, finish=j)

        a[0], a[j - 1] = a[j - 1], a[0]


if __name__ == '__main__':
    main()
