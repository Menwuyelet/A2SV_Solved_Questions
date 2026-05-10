class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num = []

        for row in matrix:
            num.extend(row)
        

        return nsmallest(k, num)[-1]