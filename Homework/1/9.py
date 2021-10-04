def from_adjacency_matrix_to_adjacency_list_undirected(matrix, start=0):
    n = len(matrix)

    adjacency_list = [[] for i in range(n + start)]

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                adjacency_list[i + start].append(j + start)
                adjacency_list[j + start].append(i + start)

    return adjacency_list


if __name__ == '__main__':
    n = int(input())
    start = 1

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    adjacency_list = from_adjacency_matrix_to_adjacency_list_undirected(matrix, start)

    for i in range(start, n + start):
        print(*adjacency_list[i])
