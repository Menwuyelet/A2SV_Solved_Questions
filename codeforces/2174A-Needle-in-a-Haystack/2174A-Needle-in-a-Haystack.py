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