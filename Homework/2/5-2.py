def solve(n, matrix):
    lst = [0]

    for i in range(1, n):
        lst.append(max([lst[j] + matrix[j][i] for j in range(0, i)]))

    return lst[-1]


if __name__ == '__main__':
    file = open('input6.txt').read().split('\n')

    n = int(file[0])

    matrix = []

    for i in range(n):
         matrix.append(list(map(int, file[i + 1].split())))

    answer = solve(n, matrix)

    print(answer)
