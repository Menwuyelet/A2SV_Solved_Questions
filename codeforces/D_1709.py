"""
- The question: given two lists we are tasked to make the lists follow strict rule.
                - the rule is that for each i, a[i] < b[i], a[i] < a[i+1], b[i] < b[i+1]
                - we can perform an operation to make the two lists follow this strict rule within 1709 moves.
                - the operations are to swap a[i] and a[i+1], swap b[i] and b[i+1] and swap a[i] and b[i]
                - and we are tasked to return the number of operations and the operations we performed.
- Solution:
    - this problem seems hard but it really is just implementation of bubble sort.
    - we sort list a with bubble sort and count the swaps we made and store the swaps we made.
    - the same for list b.
    - and finally we iterate over the two lists and we check if the two lists are sorted together meaning a[i] < b[i]
    - and if not we just swap them and add the count and the operation to our answer.
    - this is possible because of the constraints are small and the solution with O(n^2) will pass.
-  Time and Space complexity:
    - Time => O(n^2), n = len(a) == len(b)
    - space = O(1), no more than 1709 operations will not performed
"""

for _ in range(int(input())):
    n = int(input())

    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]

    count = 0
    res = []
    i = 0

    # we sort the list a by bubble sort and count the swaps
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

    # we sort the list b by bubble sort and count the swaps
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

    # we sort the two lists together
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            count += 1
            res.append([3, i + 1])

    # print our number of operations and the operations
    print(count)
    for _ in res:
        print(*_)
