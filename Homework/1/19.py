def check_parallel_edges_from_edges_list_directed(n, m, edges_list, start):
    lst = [[0 for j in range(n + start)] for i in range(n + start)]

    for edge in edges_list:
        i, j = edge
        if lst[i][j] == 1:
            return True
        lst[i][j] = 1

    return False


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    start = 1

    edges = []

    for i in range(m):
        edges.append(list(map(int, input().split())))

    have_parallel_edges = check_parallel_edges_from_edges_list_directed(n, m, edges, 1)

    if have_parallel_edges:
        print("YES")
    else:
        print("NO")
