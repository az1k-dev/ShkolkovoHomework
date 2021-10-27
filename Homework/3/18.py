def heapify(a, i=0, finish=None, start=False, key=lambda s: s):
    if finish is None:
        finish = len(a)

    i1 = i * 2 + 1
    i2 = i * 2 + 2

    if not i1 < finish:
        return

    if not i2 < finish:
        if key(a[i1]) > key(a[i]):
            a[i], a[i1] = a[i1], a[i]
        return

    if start:
        heapify(a, i1, finish, start, key)
        heapify(a, i2, finish, start, key)

    if key(a[i1]) > key(a[i]) or key(a[i2]) > key(a[i]):
        s = i1 if key(a[i1]) > key(a[i2]) else i2

        a[i], a[s] = a[s], a[i]
        heapify(a, s, finish, key=key)


def heap_sort(a, key=lambda s: s):
    n = len(a)

    heapify(a, start=True, key=key)

    for i in range(n):
        j = n - i

        heapify(a, finish=j, key=key)

        a[0], a[j - 1] = a[j - 1], a[0]


def main():
    n = int(input())

    a_taxi = []
    a_people = []

    s_people = input().split()
    s_taxi = input().split()

    for i in range(n):
        a_people.append((i + 1, int(s_people[i])))

    for i in range(n):
        a_taxi.append((i + 1, int(s_taxi[i])))

    heap_sort(a_taxi, key=lambda s: s[1])
    heap_sort(a_people, key=lambda s: s[1])

    a_people = a_people[::-1]

    a_answer = []

    for i in range(n):
        a_answer.append((a_taxi[i], a_people[i]))

    heap_sort(a_answer, key=lambda s: s[1][0])

    for i in range(n):
        print(a_answer[i][0][0], end=' ')


if __name__ == '__main__':
    main()
