for i in range(int(input())):
    a, b = map(int, input().split())
    Ba = input()
    Bb = input()
    ans = []
    j =0
    for i in range(a):
        while j < b:
            if Ba[i] == Bb[j]:
                ans.append(Ba[i])
                j += 1
                break
            j += 1
        if j >= b:
            break

    print(len(ans))