def is_regular_graph(n, m, edges_list, start):
    check_list = [0 for i in range(n + start)]

    for edge in edges_list:
        i, j = edge
        check_list[i] += 1
        check_list[j] += 1

    is_regular = all(map(lambda s: s == check_list[start], check_list[start:]))

    return is_regular


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    start = 1

    edges = []

    for i in range(m):
        edges.append(list(map(int, input().split())))

    is_regular = is_regular_graph(n, m, edges, start)

    if is_regular:
        print("YES")
    else:
        print("NO")
