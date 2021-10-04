def from_edges_list_to_adjacency_list_directed(n, m, edges, start=0):
    adjacency_list = [[] for i in range(n + start)]

    for edge in edges:
        i, j = edge
        adjacency_list[i].append(j)

    return adjacency_list


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    start = 1

    edges = []

    for i in range(m):
        edges.append(list(map(int, input().split())))

    adjacency_list = from_edges_list_to_adjacency_list_directed(n, m, edges, start)

    for s in adjacency_list:
        print(*s)
