# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort()
#         h_indx = 0
#         n = len(citations)

#         for indx, citation in enumerate(citations):
#             if (n - indx) >= citation:
#                 h_indx = citation
            
#         return h_indx

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        
        return 0