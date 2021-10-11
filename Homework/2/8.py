def find_longest(adjacency_list, v, parent=None):
    if len(adjacency_list[v]) == 1:
        return (v, 0), (None, None, 0)

    longest_into = (None, None, 0)

    max1 = (None, 0)
    max2 = (None, 0)

    for i in adjacency_list[v]:
        if i == parent:
            continue

        s = find_longest(adjacency_list, i, v)

        if s[1][2] > longest_into[2]:
            longest_into = s[1]

        if s[0][1] + 1 > max1[1]:
            max2 = max1
            max1 = (s[0][0], s[0][1] + 1)
        elif s[0][1] + 1 > max2[1]:
            max2 = (s[0][0], s[0][1] + 1)

    if longest_into[2] < max1[1] + max2[1]:
        longest_into = (max1[0], max2[0], max1[1] + max2[1])

    return max1, longest_into


if __name__ == '__main__':
    file = open('input9.txt').read().split('\n')

    v, e = list(map(int, file[0].split()))

    adjacency_list = [[] for i in range(v)]

    for i in range(e):
        a, b = list(map(lambda s: int(s) - 1, file[i + 1].split()))

        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    answer = find_longest(adjacency_list, 0)

    print(*sorted(list(map(lambda s: s + 1, answer[1][:2]))))
