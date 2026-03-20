"""
- The question: given two strings s and t, we need to determine if we can rearrange the characters of t to form a new string t' 
                - such that it is lexicographically smaller than other possible arrangements of t and also contains s as a subsequence.
                - if it is possible, we return the lexicographically smallest arrangement of t else we return "Impossible"
- Solution:
    - since we need to check if s can be a subsequence of t, we first count the frequency of characters in both s and t and compare.
    - if the frequency of any character in s is greater than its frequency in t, then it is impossible to form t' and we return "Impossible"
    - if it is possible, we build t' by taking the characters in t that are not in s and sort them.
    - finally, we merge s and the sorted t' to get the lexicographically smallest result by comparing characters from both strings and appending the smaller one to the result.
    - if equal we take character form s.
-  Time and Space complexity:
    - Time => O(m log(m)), since we are sorting m = len(t) - len(s)
    - space = O(m)
"""



from collections import Counter

for _ in range(int(input())):
    s = input().strip()
    t = input().strip()

    count_s = Counter(s)
    count_t = Counter(t)

    # we check feasibility 
    for ch in count_s:
        if count_s[ch] > count_t[ch]:
            print("Impossible")
            break

    else:

        # build t' which is t without the characters in s
        remaining = []
        for ch in count_t:
            extra = count_t[ch] - count_s[ch]
            remaining.extend([ch] * extra)

        t_prime = sorted(remaining)

        # merge s and t' to get the lexicographically smallest result
        i = j = 0
        res = []

        while i < len(s) and j < len(t_prime):
            if s[i] < t_prime[j]:
                res.append(s[i])
                i += 1
            elif s[i] > t_prime[j]:
                res.append(t_prime[j])
                j += 1
            else:
                # if they are equal we take s
                res.append(s[i])
                i += 1

        # append leftovers
        res.extend(s[i:])
        res.extend(t_prime[j:])

        print("".join(res))