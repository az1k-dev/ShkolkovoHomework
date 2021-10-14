def heapify(heap, i=0, finish=None, start=False):
    if finish is None:
        finish = len(heap)

    if not i * 2 + 1 < finish:
        return

    if not i * 2 + 2 < finish:
        if heap[i] < heap[i * 2 + 1]:
            heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
        return

    if start:
        heapify(heap, i * 2 + 1, finish, start=start)
        heapify(heap, i * 2 + 2, finish, start=start)

    if heap[i] < heap[i * 2 + 1] or heap[i] < heap[i * 2 + 2]:
        if heap[i * 2 + 1] < heap[i * 2 + 2]:
            heap[i], heap[i * 2 + 2] = heap[i * 2 + 2], heap[i]
            heapify(heap, i * 2 + 2, finish)
        else:
            heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
            heapify(heap, i * 2 + 1, finish)


def heap_sort(a):
    n = len(a)

    heapify(a, start=True)

    print(a)

    for i in range(n):
        j = n - i
        print("a)", a)
        heapify(a, finish=j)
        print("b)", a)
        a[0], a[j - 1] = a[j - 1], a[0]
        print("c)", a)

    return


if __name__ == '__main__':
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    heap_sort(lst)

    print(lst)
