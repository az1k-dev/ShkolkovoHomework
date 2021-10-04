def reverse_graph_by_adjacency_list(n, adjacency_list, start):
    new_adjacency_list = [[] for i in range(n + start)]

    for i in range(n):
        for j in adjacency_list[i]:
            new_adjacency_list[j].append(i + start)

    return new_adjacency_list


if __name__ == '__main__':
    n = int(input())
    start = 1

    adjacency_list = []

    for i in range(n):
        adjacency_list.append(list(map(int, input().split())))

    new_adjacency_list = reverse_graph_by_adjacency_list(n, adjacency_list, start)

    for i in range(start, n + start):
        print(*new_adjacency_list[i])
