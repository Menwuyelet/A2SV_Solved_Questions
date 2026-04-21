"""
- The question: we are given a list of numbers and tasked to generat a list of subsets that follows the rules, 
                - the subsets should be in non decreasing order.
                - the subset should be atleast len of 2.
- Solution:
    - this is generaly a enumeration backtracking problem, 
    - we could solve it with using a normal sub set generation approach we just need to add a condition that check the condition of non decreasing order and the length to be more than 1.
    - that is it.
-  Time and Space complexity:
    - Time = O(2^n * n^2), n = len(nums)
    - space = O(n * 2^n), 
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backtrack(start, curr):
            
            # we check if the current sub set is length of 2 or more and if so append it to our answer
            if len(curr) >= 2:
                ans.add(tuple(curr[:]))
            
            # our base case to return if the current subset is equal to the original list
            if len(curr) == len(nums):
                return

            for i in range(start, len(nums)):

                # we check the condition of that the curr list follows the non decreasing order
                if (curr and nums[i] >= curr[-1]) or not curr:
                    curr.append(nums[i])
                    backtrack(i+1, curr)
                    curr.pop()

        
        backtrack(0, [])

        return list(ans)


