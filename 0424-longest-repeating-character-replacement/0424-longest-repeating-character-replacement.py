class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans = 0
        left = 0
        maxcount = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxcount = max(maxcount, count[s[right]])

            while (right - left + 1) - maxcount > k:
                count[s[left]]-= 1
                left += 1
                
            ans = max(ans, right - left + 1)

        return ans