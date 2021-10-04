def from_adjacency_list_to_adjacency_matrix_undirected(n, adjacency_list, start):
    matrix = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in adjacency_list[i]:
            matrix[i][j - start] = 1
            matrix[j - start][i] = 1

    return matrix


if __name__ == '__main__':
    n = int(input())
    start = 1

    adjacency_list = []

    for i in range(n):
        adjacency_list.append(list(map(int, input().split())))

    matrix = from_adjacency_list_to_adjacency_matrix_undirected(n, adjacency_list, start)

    for row in matrix:
        print(*row)
