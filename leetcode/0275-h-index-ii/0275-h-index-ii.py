class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        for idx, citation in enumerate(citations):
            if citation >= n - idx:
                return n - idx
        
        return 0
