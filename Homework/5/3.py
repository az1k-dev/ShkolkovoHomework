def solution():
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))[1:]
    c = len(lst)
    a = k

    break_lst = []

    while a < n:
        last_break_id = -1
        if break_lst:
            last_break_id = break_lst[-1]

        new_break = None

        for i in range(last_break_id + 1, c):
            if lst[i] <= a:
                new_break = i
            else:
                break

        if new_break is None:
            return -1
        else:
            a = lst[new_break] + k
            break_lst.append(new_break)

    return len(break_lst)


print(solution())
