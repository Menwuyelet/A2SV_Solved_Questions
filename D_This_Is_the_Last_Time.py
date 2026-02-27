"""
- The question: given a list of casinos we are tasked to maximize the coin we will have at the end of visiting any of the cassinos. possibly zero or all.

- Solution:
    - this is really easy question that looks like hard.
    - what we want to do is take the posible max coin giving casino and visit is and update our coin to that reali.
    - to do that we can sort it and take the casino with the largest reali.
    - but the treak is once we update our k, there might be new casino that we can explore and possibly maximize our k.
    - to check that the brute force would be iterating everytime we update our k to check available cassinos.
    - but this leads to n^2 time complexity.
    - we can take this approach and twik it, by sorting the cassinos by thire li and iterating over them and updating our k when we find greater reali
    - this ensures that even after updating our k we still gona see the newl and already available cassinos ensuring geting the optimal answer.
-  Time and Space complexity:
    - Time => O(n log n) due to sorting the list of contests
    - space = O(n log n), due to sorting
"""
for _ in range(int(input())):
    n, k = map(int,input().split())
    cassinos = [(list(map(int,input().split()))) for i in range(n)]

    # by sorting the increasing order of the li, we insure that we can update our coin (k) and we still be able to process the rest of the list by the updated coin.
    cassinos.sort()


    for li,ri,reali in cassinos:

        # if the current coin is greater than the li of the current cassino and the coin of the cassino is greater than our current k we update our k
        if k >= li and reali > k:
            k = reali

    print(k)