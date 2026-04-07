class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(idx, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return 
            
            for i in range(idx, n):
                curr.append(i+1)
                backtrack(i+1, curr)
                curr.pop()
            
        backtrack(0, [])
        return ans