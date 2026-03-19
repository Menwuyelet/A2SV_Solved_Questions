from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        counter_p = Counter(p)
        k = len(p)
        window = Counter(s[:k])

        if window == counter_p:
            result.append(0)

        left = 0

        for right in range(k, len(s)):
            window[s[right]] += 1
            window[s[left]] -= 1

            if window == counter_p:
                result.append(left+1)

            left += 1
                   
        return result
