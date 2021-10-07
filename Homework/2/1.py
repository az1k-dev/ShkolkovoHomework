MOVE_FUNCTIONS = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1)
]


def is_correct(x, y, g):
    return 0 <= x < len(g[0]) and 0 <= y < len(g)


def is_visited(x, y, visited):
    return visited[y][x]


def is_wall(x, y, g):
    return g[y][x] == '#'


def is_s(x, y, g):
    return g[y][x] == 's'


def is_e(x, y, g):
    return g[y][x] == 'e'


def dfs(x, y, g, visited=None, k=True):
    if visited is None:
        visited = [[False for i in range(len(g[0]))] for j in range(len(g))]

    if is_s(x, y, g):
        if k:
            return [(x, y)]
        else:
            return visited, [(x, y)]

    visited[y][x] = True

    for f in MOVE_FUNCTIONS:
        new_x, new_y = f(x, y)
        if is_correct(new_x, new_y, g) and not is_visited(new_x, new_y, visited) and not is_wall(new_x, new_y, g):

            visited, final_path = dfs(new_x, new_y, g, visited=visited, k=False)
            if final_path:
                if k:
                    return final_path
                else:
                    return visited, [(x, y)] + final_path

    if k:
        return False
    else:
        return visited, False


def bfs(x, y, g):
    queue = [(x, y)]

    visited = [[False for i in range(len(g[0]))] for j in range(len(g))]
    path = []
    dist = [[float('inf') for i in range(len(g[0]))] for j in range(len(g))]
    dist[y][x] = 0

    while queue:
        x, y = queue.pop(0)

        if is_visited(x, y, visited):
            continue

        if is_s(x, y, g):
            fx, fy = x, y
            break

        path.append((x, y))

        visited[y][x] = True

        for f in MOVE_FUNCTIONS:
            new_x, new_y = f(x, y)

            if is_correct(new_x, new_y, g) and not is_visited(new_x, new_y, visited) and not is_wall(new_x, new_y, g):
                if dist[new_y][new_x] > dist[y][x] + 1:
                    dist[new_y][new_x] = dist[y][x] + 1
                queue.append((new_x, new_y))

    path = [(fx, fy)]

    while True:
        x, y = path[-1]

        if is_e(x, y, g):
            path.append((x, y))
            break

        s = dist[y][x]

        for f in MOVE_FUNCTIONS:
            new_x, new_y = f(x, y)
            if is_correct(new_x, new_y, g) and not is_wall(new_x, new_y, g):
                if s == dist[new_y][new_x] + 1:
                    path.append((new_x, new_y))
                    break

    return path


def draw_path(path, g):
    g = g.copy()

    r = [i.copy() for i in g]

    for cell in path:
        x, y = cell
        if r[y][x] not in 'es':
            r[y][x] = '*'

    for i in range(len(r)):
        r[i] = ''.join(r[i])

    return '\n'.join(r)


if __name__ == '__main__':
    file = open('input1.txt', 'r').read().split('\n')

    w, h = list(map(int, file[0].split()))

    lst = []

    for i in range(h):
        lst.append(list(file[i + 1]))

    x, y = None, None

    for i in range(h):
        if x:
            break
        for j in range(w):
            if is_e(j, i, lst):
                x, y = j, i
                break

    path_dfs = dfs(x, y, lst)
    path_bfs = bfs(x, y, lst)

    print(draw_path(path_dfs, lst))
    print()
    print(draw_path(path_bfs, lst))
