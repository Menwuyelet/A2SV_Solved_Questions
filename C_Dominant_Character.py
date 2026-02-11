"""
- The question: given a string of len n containing chrs a, b and c we are tasked to find the smallest length of a substring that sattisfies:
    . Length of the substring is at least 2
    . 'a' occurs strictly more times in this substring than 'b'
    . 'a' occurs strictly more times in this substring than 'c'
- Solution:
    - fro the observations we can see that the longest such substring can be of len 7,
    - so we can check for all the possible permutations of such substring by if statments and check if they are in the string or not.
    - if they are we print theire length and continue to the next test case.
    - else we print -1.
-  Time and Space complexity:
    - Time => O(n), we check for a constant number of permutations and each check takes O(n) time.
    - space = O(1), we only use a constant amount of space to store the inputs.
"""

for _ in range(int(input())):
    n = int(input())
    s = input()

    if "aa" in s:
        print(2)

    # other permutations like 'caa' and 'aab' are already covered by the above condition
    elif "aca" in s or "aba" in s:
        print(3)

    # other permutations like 'aca' and 'aba' are already covered by the above condition
    elif "abca" in s or "acba" in s:
        print(4)

    # other permutations like 'abca' and 'acba' are already covered by the above condition
    elif "abbacca" in s or "accabba" in s:
        print(7)
    else:
        print(-1)
