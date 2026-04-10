"""
- The question: we are given list of integers and tasked tor generate all the permtuations of the list and return them.
- Solution:
    - we could just used pow() method and be done with this problem.
    - but the reason we are tasked to do this is to impliment our oun function using recursion or bit manipulation.
    - this is basicaly an enumration backtracking problem.
    - we use backtracking to enumerate all the permtuations and return them as a list.
-  Time and Space complexity:
    - Time = O(n*n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(remaining, curr):

            # our base case when our remaining is empty we add the current permituation to our ans and return to our caller
            if not remaining:
                ans.append(curr[:])
                return
            
            # we iterate over the remining numbers and append the current number to our curr and call our backtracking updating the remaining removing the curren element
            for i in range(len(remaining)):
                curr.append(remaining[i])

                # we go further to build the current permituation
                backtrack(remaining[:i] + remaining[i+1:], curr)

                # after we get our permituation we pop from it to go to the next permituation
                curr.pop()
            
        # we call the backtrack func with empty curr and all the numbers we are given
        backtrack(nums, [])

        return ans

