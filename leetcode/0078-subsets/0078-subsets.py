"""
- The question: we are given list of integers and tasked to return the list of all the sub sets.
- Solution:
    - this is generaly a enumeration backtracking problem, 
    - we solve it using that concept, we iterate over all the values and append them to curr
    - we append these curr lists to our answer list, our base case is when the curr length become equal to the len of nums(the original list become the subset)
    - when we hit that we return and chekc the next subset starting on the next value
-  Time and Space complexity:
    - Time = O(n*n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(num, curr):
            
            # we append the current list to our answer
            ans.append(curr[:])

            # if our curr len equal to be len of our original nums we hit our base case so we return 
            if len(curr) == len(nums):
                return

            # we iterate over the original list and construct the subset list
            for i in range(len(num)):
                # we append the current num and calls our backtracking updating our num moving to right 1 posision
                curr.append(num[i])
                backtrack(num[i+1:], curr)

                # we pop from our curr to get other subsets
                curr.pop()
            
        
        backtrack(nums, [])
        return ans