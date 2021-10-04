def have_a_loop(matrix):
    n = len(matrix)

    for i in range(n):
        if matrix[i][i] == 1:
            return True

    return False


if __name__ == '__main__':
    n = int(input())

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    if have_a_loop(matrix):
        print("YES")
    else:
        print("NO")
