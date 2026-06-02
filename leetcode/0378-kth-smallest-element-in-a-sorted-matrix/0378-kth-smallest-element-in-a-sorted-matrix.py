class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num = []

        for row in matrix:
            num.extend(row)

        return nsmallest(k, num)[-1]
        # n = len(matrix)

        # return nsmallest(k, num, key= matrix[i // n][i % n]: for i in range(n))[-1]