class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_indx = 0
        n = len(citations)
        
        if n == 1:
            return 1

        for indx, citation in enumerate(citations):
            if (n - indx) + 1 >= citation:
                h_indx = citation
            
        return h_indx