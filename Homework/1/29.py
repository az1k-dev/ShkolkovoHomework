def from_edges_list_to_adjacency_matrix_undirected(n, m, edges, start=0):
    matrix = [[0 for i in range(n)] for j in range(n)]

    for edge in edges:
        i, j = edge
        matrix[i - start][j - start] += 1
        matrix[j - start][i - start] += 1

    return matrix


def is_transitive_undirected(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            for s in range(n):
                if i == s:
                    continue
                if matrix[i][j] and matrix[j][s] and not matrix[i][s]:
                    return False

    return True


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    start = 1

    edges = []

    for i in range(m):
        edges.append(list(map(int, input().split())))

    matrix = from_edges_list_to_adjacency_matrix_undirected(n, m, edges,
                                                          start)

    is_transitive = is_transitive_undirected(matrix)

    if is_transitive:
        print("YES")
    else:
        print("NO")
