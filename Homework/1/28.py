def from_edges_list_to_adjacency_matrix_directed(n, m, edges, start=0):
    matrix = [[0 for i in range(n)] for j in range(n)]

    for edge in edges:
        i, j = edge
        matrix[i - start][j - start] += 1

    return matrix


def is_tournament_graph(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] + matrix[j][i] != 1:
                return False

    return True


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    start = 1

    edges = []

    for i in range(m):
        edges.append(list(map(int, input().split())))

    matrix = from_edges_list_to_adjacency_matrix_directed(n, m, edges, start)

    is_tournament = is_tournament_graph(matrix)

    if is_tournament:
        print("YES")
    else:
        print("NO")
