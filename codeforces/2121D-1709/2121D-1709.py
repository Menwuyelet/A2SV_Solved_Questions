for _ in range(int(input())):
    n = int(input())

    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]

    count = 0
    res = []
    i = 0
    while True:
        move = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                count += 1
                move += 1
                res.append([1, i + 1])

        if not move:
            break

    i = 0
    while True:
        move = 0
        for i in range(n - 1):
            if b[i] > b[i + 1]:
                b[i], b[i + 1] = b[i + 1], b[i]
                count += 1
                move += 1
                res.append([2, i + 1])

        if not move:
            break

    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            count += 1
            res.append([3, i + 1])

    print(count)
    for _ in res:
        print(*_)