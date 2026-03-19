"""
- The question: given a list of citations we are tasked to find the h index of the autor. the h index is:
                    - The h-index is the maximum h such that the researcher has at least h papers with ≥ h citations each.
- Solution:
    - since what we want is the maximum h with atleast h citations having the same or above citations, 
    - we sort it in increasing order and iterate through it and compare ith value and len(citations) - i, ith value is greater or equal to len(citations) - i we return len(citations) - i as our answer.
    - else we reach the end of the list, we return 0 as our answer.
-  Time and Space complexity:
    - Time = O(n log n), n = len(citations),
    - space = O(1) 
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        
        return 0
