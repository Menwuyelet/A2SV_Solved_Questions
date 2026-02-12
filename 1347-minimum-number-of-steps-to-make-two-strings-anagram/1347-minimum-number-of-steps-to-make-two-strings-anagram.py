class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        ans  = 0
        for key in count_s:
            if count_s[key] >= count_t[key]:
                ans += count_s[key] - count_t[key]
            
        return ans