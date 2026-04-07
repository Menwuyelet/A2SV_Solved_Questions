"""
- The question: we are given two integers n and k and tasked to return all the combinations of numbers from 1 to n with length of k.
- Solution:
    - this problem is a combination backtracking problem we could solve using recurssion(backtracking)
    - we start with a base case of length of the current array equals to our k and we append that current array to our answer.
    - we use a for loop to add new elements starting with our starting indx up to n. we start with 0
    - 
-  Time and Space complexity:
    - Time = O(C(n, k) × k), number of combinations
    - space = O(C(n, k) × k), 
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        

        def backtrack(idx, curr):

            # this is our base case that when the current length is equal to our length limit
            if len(curr) == k:

                # we append by copying it because we edit the curr array in the next iteration
                ans.append(curr[:])
                return 
            
            # we run the for loop to iterate over the all numbers between the current indx and our n and add them backtracking.
            max_idx = n - (k - len(curr)) + 1 
            for i in range(idx, max_idx):

                # we add our current idx + 1 to our current
                curr.append(i+1)

                # we backtrack to continue the opration for other numbers
                backtrack(i+1, curr)

                # after backtracking we pop the last element and continue to the next ieration
                curr.pop()
            
        
        # we call the backtracking with indx 0 and empty current array
        backtrack(0, [])

        return ans