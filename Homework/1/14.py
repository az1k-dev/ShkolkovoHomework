def from_adjacency_list_to_edges_list_undirected(n, adjacency_list, start=0):
    edges_list = []

    for i in range(n):
        for j in adjacency_list[i]:
            if i < j:
                edges_list.append((i + start, j))

    return edges_list


if __name__ == '__main__':
    n = int(input())
    start = 1

    adjacency_list = []

    for i in range(n):
        adjacency_list.append(list(map(int, input().split())))

    edges_list = from_adjacency_list_to_edges_list_undirected(n, adjacency_list, start)

    for pair in edges_list:
        print(*pair)
