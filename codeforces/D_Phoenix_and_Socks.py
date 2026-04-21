from collections import Counter

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    left = Counter(socks[:l])
    right = Counter(socks[l:])

    # Step 1: remove matching pairs
    for c in list(left.keys()):
        m = min(left[c], right[c])
        left[c] -= m
        right[c] -= m
        l -= m
        r -= m

    # Step 2: ensure l >= r
    if l < r:
        left, right = right, left
        l, r = r, l

    ans = 0

    # Step 3: fix imbalance
    # diff = l - r
    # for c in left:
    #     if diff <= 0:
    #         break
    #     pairs = left[c] // 2
    #     take = min(pairs, diff // 2)
    #     ans += take
    #     left[c] -= take * 2
    #     diff -= take * 2

    # Step 4: remaining imbalance
    ans += (l - r) // 2

    # # Step 5: recolor remaining
    ans += (l + r) // 2

    print(ans)