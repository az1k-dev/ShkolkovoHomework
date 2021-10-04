def is_transitive_directed(matrix):
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
    n = int(input())

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    is_transitive = is_transitive_directed(matrix)

    if is_transitive:
        print("YES")
    else:
        print("NO")
