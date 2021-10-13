def check_ar(a):
    n = len(a)

    for i in range(1, n):
        if a[i] > a[i - 1]:
            return i

    return None


if __name__ == '__main__':
    n = int(input())

    lst = list(map(int, input().split()))

    answer = check_ar(lst)

    if answer:
        print(answer + 1)
    else:
        print('No pupupu')
