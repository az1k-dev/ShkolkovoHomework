def degrees_of_vertices_from_edges_list_undirected(n, m, edges_list, start):
    degrees_of_vertices = [[0, 0] for i in range(n + start)]

    for edge in edges_list:
        i, j = edge
        degrees_of_vertices[i][1] += 1
        degrees_of_vertices[j][0] += 1

    return degrees_of_vertices


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    start = 1

    edges = []

    for i in range(m):
        edges.append(list(map(int, input().split())))

    degrees_of_vertices = degrees_of_vertices_from_edges_list_undirected(n, m, edges, start)

    for pair in degrees_of_vertices[start:]:
        print(*pair)
