def sameParity(a, b):
    parA = 0 if a%2 == 0 else 1
    parB = 0 if b%2 == 0 else 1

    return parA == parB

for i in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    sortedNum = sorted(num) 

    for i in range(n):
        if not sameParity(num[i], sortedNum[i]):
            print("NO")
            break
    else:
        print("YES")