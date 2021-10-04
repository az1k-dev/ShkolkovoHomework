def from_adjacency_matrix_to_edges_list_directed(matrix, start=0):
    n = len(matrix)

    edges = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges.append((i + start, j + start))

    return edges


if __name__ == '__main__':
    n = int(input())
    start = 1

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    edges = from_adjacency_matrix_to_edges_list_directed(matrix, start)

    for edge in edges:
        print(*edge)
