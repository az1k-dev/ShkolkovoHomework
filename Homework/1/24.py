def sources_and_stocks_from_adjacency_matrix_directed(matrix, start):
    n = len(matrix)

    sources = []
    stocks = []

    for i in range(n):
        if all(map(lambda s: s == 0, matrix[i])):
            stocks.append(i + start)
        if all(map(lambda s: s == 0, [matrix[k][i] for k in range(n)])):
            sources.append(i + start)

    return sources, stocks


if __name__ == '__main__':
    n = int(input())
    start = 1

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    sources, stocks = sources_and_stocks_from_adjacency_matrix_directed(matrix, start)

    print(len(sources), *sources)
    print(len(stocks), *stocks)
