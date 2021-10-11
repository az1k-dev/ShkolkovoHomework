def bfs(start):
    queue = [(start, 0)]

    while queue:
        v, s = queue.pop(0)

        if d[start][v] is None:
            d[start][v] = s

            for i in adjacency_list[v]:
                if d[start][i] is None:
                    queue.append((i, s + 1))


if __name__ == '__main__':
    file = open('input10.txt').read().split('\n')

    v, e = list(map(int, file[0].split()))

    adjacency_list = [[] for i in range(v)]

    for i in range(e):
        a, b = list(map(lambda s: int(s) - 1, file[i + 1].split()))

        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    d = [[None for i in range(v)] for j in range(v)]

    for i in range(v):
        bfs(i)

    max_s = 0
    a, b = None, None

    for i in range(v):
        for j in range(v):
            if d[i][j] is None:
                continue
            if d[i][j] > max_s:
                a, b = i, j
                max_s = d[i][j]

    print(a + 1, b + 1)
