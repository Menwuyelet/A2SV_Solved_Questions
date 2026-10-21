for i in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    count = {'1':0, '0':0}
    l,r = 0, 0
    while r < k-1:
        count[s[r]] += 1
        r += 1
    ans = 0
    if count["1"] > 0:
        ans += 1
    while r < n:
        if s[r] == "1":
            if count[s[r]] == 0:
                ans += 1
            
        count[s[r]] += 1
        count[s[l]] -= 1
        r += 1
        l += 1
    print(ans)