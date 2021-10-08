def dfs(stack, adjacency_list, visited=None):
    if visited is None:
        visited = [False for i in range(len(adjacency_list))]

    visited[stack[-1]] = True

    for i in adjacency_list[stack[-1]]:
        if stack[0] == i:
            return stack
        if not visited[i]:
            s = dfs(stack + [i], adjacency_list, visited)
            if s:
                return s

    return False


if __name__ == '__main__':
    file = open('input3.txt').read().split('\n')

    v, e = list(map(int, file[0].split()))

    adjacency_list = [[] for i in range(v + 1)]

    for i in range(e):
        a, b = list(map(int, file[i + 1].split()))
        adjacency_list[a].append(b)

    cycle = False

    for i in range(1, v + 1):
        cycle = dfs([i], adjacency_list)
        if cycle:
            break

    if cycle:
        print("YES")
        print(*cycle)
    else:
        print("NO")
