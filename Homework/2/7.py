def dfs(stack, adjacency_list):
    for i in adjacency_list[stack[-1]]:
        if len(stack) >= 2:
            if i in stack[:-2]:
                return False
            if i == stack[-2]:
                continue

        if not dfs(stack + [i], adjacency_list):
            return False

    return True


if __name__ == '__main__':
    file = open("input8.txt").read().split('\n')

    v, e = list(map(int, file[0].split()))

    adjacency_list = [[] for i in range(v)]

    for i in range(e):
        a, b = list(map(lambda s: int(s) - 1, file[i + 1].split()))
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    if dfs([0], adjacency_list):
        print("YES")
    else:
        print("NO")
