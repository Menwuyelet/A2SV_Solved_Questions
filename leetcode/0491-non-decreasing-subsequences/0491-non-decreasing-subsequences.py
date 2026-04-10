class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backtrack(start, curr):

            if len(curr) >= 2:
                ans.add(tuple(curr[:]))
            
            if len(curr) == len(nums):
                return

            for i in range(start, len(nums)):
                if (curr and nums[i] >= curr[-1]) or not curr:
                    curr.append(nums[i])
                    backtrack(i+1, curr)
                    curr.pop()

        
        backtrack(0, [])

        return list(ans)


