def dijkstra(n, matrix):
    d = [float('inf') for i in range(n)]
    visited = [False for i in range(n)]
    parents = [None for i in range(n)]

    d[0] = 0

    while True:
        v_min = float("inf")
        v = None

        for i in range(n):
            if not visited[i] and v_min > d[i]:
                v_min = d[i]
                v = i

        if v is None:
            break

        if v == n - 1:
            break

        for i in range(n):
            if d[v] + matrix[v][i] < d[i]:
                d[i] = d[v] + matrix[v][i]
                parents[i] = v

        visited[v] = True

    lst = []

    s = n - 1

    while s is not None:
        lst.append(s)
        s = parents[s]

    return d[n - 1], len(lst) - 1


if __name__ == '__main__':
    file = open('input5.txt').read().split('\n')

    n = int(file[0])

    matrix = []

    for i in range(n):
         matrix.append(list(map(int, file[i + 1].split())))

    answer = dijkstra(n, matrix)

    print(*answer)
