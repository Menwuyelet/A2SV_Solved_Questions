class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or strs[0][i] != word[i]:
                    return ("").join(ans) if ans else ""
            ans.append(word[i])
        return ("").join(ans) if ans else ""