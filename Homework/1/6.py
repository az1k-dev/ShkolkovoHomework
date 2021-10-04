def from_edges_list_to_adjacency_matrix_undirected(edges, n, m, start=0):
    matrix = [[0 for i in range(n)] for j in range(n)]

    for edge in edges:
        i, j = edge
        matrix[i - start][j - start] += 1
        matrix[j - start][i - start] += 1

    return matrix


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    start = 1

    edges = []

    for i in range(m):
        edges.append(list(map(int, input().split())))

    matrix = from_edges_list_to_adjacency_matrix_undirected(edges, n, m, start)

    for row in matrix:
        print(*row)
