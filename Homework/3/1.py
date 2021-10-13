def bubble_sort(a):
    n = len(a)

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                print(i, j)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))

    bubble_sort(lst)
