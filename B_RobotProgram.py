import sys
input = sys.stdin.readline


for _ in range(int(input()):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pref = 0
    first_hit = -1
    
    # finde first hit starting from x
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        
        if x + pref == 0:
            first_hit = i + 1
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    count = 1
    remaining = k - first_hit
    
    # find cycle after finding the first hit starting from 0
    pref = 0
    cycle_len = -1
    
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        
        if pref == 0:
            cycle_len = i + 1
            break
    
    if cycle_len != -1:
        count += remaining // cycle_len
    
    print(count)
