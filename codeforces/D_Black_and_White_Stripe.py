from collections import Counter
for _ in range(int(input())):
    n , k = map(int, input().split())
    string = input()

    count = string[:k].count("W")
    ans = count

    j = 0
    for i in range(k, n):
        if string[i] == "W":
            count += 1
        if string[j] == "W":
            count -= 1

        j += 1
        ans = min(count, ans) 
            
    print(ans)
