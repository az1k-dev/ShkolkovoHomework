def degrees_of_vertices_from_adjacency_matrix_undirected(matrix):
    n = len(matrix)

    degrees_of_vertices = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                degrees_of_vertices[i] += 1

    return degrees_of_vertices


if __name__ == '__main__':
    n = int(input())
    start = 1

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    degrees_of_vertices = degrees_of_vertices_from_adjacency_matrix_undirected(matrix)

    print(*degrees_of_vertices)
