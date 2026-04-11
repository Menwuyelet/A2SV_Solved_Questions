"""
- The question: we are given a list of chrs and the length of the string should be formed by the perituation tasked to return the kth string after forming the permutuations and sorting them alphabeticaly.
- Solution:
    - this is an enumrating problem.
    - we just use backtracking to construct the permituations and after that sort them and return the kth element.
    - but to avoid sorting, we could just use dictinary to map the elements with an int starting at 1 and return the value mapped to the k.
    - for further optimizing, we break the backtracking when we hit the kth element removing unassery iterations.
-  Time and Space complexity:
    - Time = O(min(2n,k*n)), n = len(nums)
    - space = O(K * n), 
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        maping = {}
        i = 1
        chrs = ['a', 'b', 'c']

        def backtrack(curr):
            nonlocal i
            if i > k:
                return 
            
            if len(curr) == n:
                # print(maping)
                maping[i] = curr[:]
                i += 1
                return
            
            for chr in chrs:
                if (curr and chr != curr[-1]) or not curr:
                    curr.append(chr)

                    backtrack(curr)
                    curr.pop()
            
        backtrack([])
        return "".join(maping[k]) if k in maping else ""