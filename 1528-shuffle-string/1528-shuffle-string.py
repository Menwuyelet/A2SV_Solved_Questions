class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0]*len(s)
        for idx, val in zip(indices, s):
            ans[idx] = val
        return "".join(ans)