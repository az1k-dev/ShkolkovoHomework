def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def sort(a):
    n = len(a)
    count = 0

    for i in range(n):
        m_i = i
        for j in range(i, n):
            if a[j] < a[m_i]:
                m_i = j
        if m_i != i:
            swap(a, m_i, i)
            count += 1

    return a, count


if __name__ == '__main__':
    n = int(input())

    lst = []

    for i in range(n):
        lst.append(int(input()))

    lst, count = sort(lst)

    print(lst, count)
