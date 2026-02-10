"""
- The question: we are given string and indices and tasked to shuffle the strings to match the given indeces.
- Solution:
    - to solve the problem we can create new list initial values and update the values as we iterate through the idices and the string.
-  Time and Space complexity:
    - Time = O(n), n = len(s)
    - space = O(n), 
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0]*len(s)
        for idx, val in zip(indices, s):
            ans[idx] = val
        return "".join(ans)