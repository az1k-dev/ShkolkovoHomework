def paint_bfs(lst):
    queue = [0]

    color = [None for i in range(len(lst))]
    color[0] = 0

    while queue:
        v = queue.pop(0)

        for i in lst[v]:
            if color[i] is None:
                color[i] = (color[v] + 1) % 2
                queue.append(i)

    return color


if __name__ == '__main__':
    file = open("input7.txt").read().split('\n')

    v, e = list(map(int, file[0].split()))

    lst = [[] for i in range(v)]

    for i in range(e):
        a, b = list(map(lambda s: int(s) - 1, file[i + 1].split()))
        lst[a].append(b)
        lst[b].append(a)

    answer = paint_bfs(lst)

    print(*answer)
