def bfs(v):
    global visited, adjacency_list
    queue = [v]

    while queue:
        v = queue.pop(0)

        visited[v] = True

        for i in adjacency_list[v]:
            if not visited[i]:
                queue.append(i)


if __name__ == '__main__':
    file = open('input4.txt').read().split('\n')

    v, e = list(map(int, file[0].split()))

    adjacency_list = [[] for i in range(v + 1)]

    for i in range(e):
        a, b = list(map(int, file[i + 1].split()))
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    visited = [False for i in range(v + 1)]

    count = 0

    for i in range(1, v + 1):
        if not visited[i]:
            bfs(i)
            count += 1

    print(count)
