MOVE_FUNCTIONS = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1)
]


def is_visited(x, y, visited):
    return visited[y][x]


def is_correct(x, y, g):
    return 0 <= x < len(g[0]) and 0 <= y < len(g)


def is_wall(x, y, g):
    return g[y][x] == '#'


def check_count(x, y, g):
    count = 0

    for f in MOVE_FUNCTIONS:
        nx, ny = f(x, y)

        if is_correct(nx, ny, g):
            count += int(g[ny][nx] == '#')

    return count


def dfs(x, y, g, visited=None, k=True):
    if visited is None:
        visited = [[False for i in range(len(g[0]))] for j in range(len(g))]

    count = check_count(x, y, g)
    visited[y][x] = True

    for f in MOVE_FUNCTIONS:
        nx, ny = f(x, y)

        if is_correct(nx, ny, g) and not is_wall(nx, ny, g) and not is_visited(nx, ny, visited):
            n_count, visited = dfs(nx, ny, g, visited, False)
            count += n_count

    if k:
        return count
    return count, visited


def bfs(x, y, g):
    visited = [[False for i in range(len(g[0]))] for j in range(len(g))]

    queue = [(x, y)]

    count = 0

    while queue:
        x, y = queue.pop(0)

        if is_visited(x, y, visited):
            continue

        count += check_count(x, y, g)
        visited[y][x] = True

        for f in MOVE_FUNCTIONS:
            nx, ny = f(x, y)

            if is_correct(nx, ny, g) and not is_wall(nx, ny, g) and not is_visited(nx, ny, visited):
                queue.append((nx, ny))

    return count


if __name__ == '__main__':
    file = open('input2.txt', 'r').read().split('\n')

    w, h = list(map(int, file[0].split()))

    lst = []

    for i in range(h):
        lst.append(list(file[i + 1]))

    x, y = None, None

    for i in range(h):
        if x:
            break
        for j in range(w):
            if lst[i][j] == 's':
                x, y = j, i
                break

    count_dfs = dfs(x, y, lst)
    count_bfs = bfs(x, y, lst)

    print(count_dfs)
    print(count_bfs)
