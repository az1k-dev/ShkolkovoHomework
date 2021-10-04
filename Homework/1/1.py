def can_be_undirected(matrix):
    n = len(matrix)

    for i in range(n):
        if matrix[i][i] == 1:
            return False

        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


if __name__ == '__main__':
    n = int(input())

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    if can_be_undirected(matrix):
        print("YES")
    else:
        print("NO")
