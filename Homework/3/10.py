def heapify(a, i=0, start=False, finish=None):
    global count
    count += 1

    if finish is None:
        finish = len(a)

    c1, c2 = i * 2 + 1, i * 2 + 2

    if not c1 < finish:
        return

    if not c2 < finish:
        if a[c1] > a[i]:
            a[i], a[c1] = a[c1], a[i]
        return

    if start:
        heapify(a, c1, start=start, finish=finish)
        heapify(a, c2, start=start, finish=finish)

    if a[i] < a[c1] or a[i] < a[c2]:
        if a[c1] > a[c2]:
            a[i], a[c1] = a[c1], a[i]
            heapify(a, c1, finish=finish)
        else:
            a[i], a[c2] = a[c2], a[i]
            heapify(a, c2, finish=finish)

    return


def heap_sort(a):
    n = len(a)

    heapify(a, start=True)

    for i in range(n, 0, -1):
        heapify(a, finish=i)
        a[0], a[i - 1] = a[i - 1], a[0]

    return


if __name__ == '__main__':
    n = 1000000

    # O(n) case
    lst = [1 for i in range(n)]

    count = 0

    heap_sort(lst)

    print(count)

    # O(n * log n) case
    lst = [i for i in range(n)]

    count = 0

    heap_sort(lst)

    print(count)
