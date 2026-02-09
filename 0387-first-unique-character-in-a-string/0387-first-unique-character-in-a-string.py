"""
- The question: given a string we are tasked to find the first chr that is appearing only onece. the chr should be the firs appearing.
- Solution:
    - this problem is very easy counting problem.
    - we can use counter to count and store the frequency of the chrs in the string and iterate through them to find the first element.
-  Time and Space complexity:
    - Time =  Sorting: O(n)
    - space = Sorting: N(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = float("inf")
        count = Counter(s)
        for i in s:
            if count[i] == 1:
                ans = min(ans, s.index(i))
        
        if ans != float("inf"):
            return ans
        else:
            return -1
            