"""
- The question: we are given list of integers and tasked to return the list of all the sub sets. this is the same problem as subsets, with only difrence being that this one might contain duplicat elements
- Solution:
    - this is generaly a enumeration backtracking problem, 
    - we solve it using that concept, we iterate over all the values and append them to curr
    - we append these curr lists to our answer list, our base case is when the curr length become equal to the len of nums(the original list become the subset)
    - when we hit that we return and chekc the next subset starting on the next value
    - to eliminate the duplication we use set instead of list to store our answer
-  Time and Space complexity:
    - Time = O(2^n * n^2), n = len(nums)
    - space = O(n*2^n), 
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # we use set to remove duplicates
        ans = set()

        def backtrack(num, curr):
            
            # we convert the curr list to tuple to allow it to be stored in set
            ans.add(tuple(curr[:]))

            if len(curr) == len(nums):
                return 


            for i in range(len(num)):
                # we append the current num and calls our backtracking updating our num moving to right 1 posision
                curr.append(num[i])
                backtrack(num[i+1:], curr)

                # we pop from our curr to get other subsets
                curr.pop()

        nums.sort()
        backtrack(nums, [])
        return list(ans)