for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pa, pb = 0, 0
    ans = 0
    while pb < n:
        if a[pa] > b[pb]:
            ans += 1
            pb += 1
        else:
            pa += 1
            pb += 1

    print(ans)