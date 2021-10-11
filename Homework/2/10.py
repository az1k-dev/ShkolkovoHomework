def solve(n, matrix, adjacency_list):
    a = []

    a.append([None for i in range(n)])

    a[0][0] = 0

    for i in range(1, n + 1):
        a.append([])

        for k in range(n):
            a[i].append(a[i - 1][k])

        for j in range(n):
            if a[i - 1][j] is not None:
                for s in adjacency_list[j]:
                    if a[i][s] is None or a[i - 1][j] + matrix[j][s] > a[i][s]:
                        a[i][s] = a[i - 1][j] + matrix[j][s]

    if a[-1] != a[-2]:
        return ":)"

    if a[-1][-1] is None:
        return ":("

    return a[-1][-1]


if __name__ == '__main__':
    file = open('input11.txt').read().split('\n')

    n, m = list(map(int, file[0].split()))

    matrix = [[None for i in range(n)] for j in range(n)]
    adjacency_list = [[] for i in range(n)]

    for i in range(m):
        a, b, c = list(map(int, file[i + 1].split()))
        a -= 1
        b -= 1

        if matrix[a][b] is None:
            matrix[a][b] = c
            adjacency_list[a].append(b)

        if matrix[a][b] < c:
            matrix[a][b] = c

    answer = solve(n, matrix, adjacency_list)

    print(answer)
