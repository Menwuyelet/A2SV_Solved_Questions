class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        left = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in count:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    count.pop(s[left])
                left += 1
            count[s[i]] = 1
            ans = max(ans, i-left+1)
        return ans