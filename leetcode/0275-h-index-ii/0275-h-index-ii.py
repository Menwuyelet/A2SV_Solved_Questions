"""
- The question: we are given a list of citations that for each citation in the ith indx is the amount of times the ith book have been cited. we are tasked to return the h-indx of the researchers.
- Solution:
    - this is prety simple problem.
    - the input is already sorted so we just need to iterate over the list and check for every citation if it satisfies citation >= n - idx, 
    - the first time we get the satisfied answer we return that citation as answer.

-  Time and Space complexity:
    - Time = O(n), n = len(citations)
    - space = O(1) 
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        for idx, citation in enumerate(citations):

            # we check if the current citation is the h-index
            if citation >= n - idx:
                return n - idx
        
        # if the citation list only contains 0 as its value
        return 0
