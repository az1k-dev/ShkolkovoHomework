def edges_count_in_directed(matrix):
    n = len(matrix)

    count = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                count += 1

    return count


if __name__ == '__main__':
    n = int(input())

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    count = edges_count_in_directed(matrix)

    print(count)
