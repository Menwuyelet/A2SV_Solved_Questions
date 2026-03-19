"""
- The question: we are given a matrix and tasked to implement NumMatrix which performs range sum with O(1) constant opration.
- Solution:
    - the brute force approach will be computing the sum by iterating from the starting cell to the ending cell every time we get query.
    - but that will be very ineficent so we use other way.
    - the other way is prefix sum(2D range update prefix sum).
    - to impliment it we first construct our prefix sum using the formula 
                - prfix_sum[i][j] = prfix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + prifix_sum[i][j]
    - after that we use the sub sum formula:
                - submatrix_sum = prefix_sum[r2][c2] − prefix_sum[r2][c1 - 1] - prefix_sum[r1 - 1][c2 ] + prefix_sum[r1 - 1][c1 - 1]
    - we use offset correction if we used extra row and column on the process of creation of the prefix_sum array
-  Time and Space complexity:
    - Time = O(n * m), n = len(matrix[0]), m = len(matrix) for the initialization, O(1) for each query after that
    - space = O(n * m)
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        # we initiate the matrix with extra column and row for our prfix sum
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        # we biuld the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix_sum[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.prefix_sum[i - 1][j]
                    + self.prefix_sum[i][j - 1]
                    - self.prefix_sum[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # i used sub_sum = [r2][r2] - [r2][c1-1] - [r1-1][c2] + [r1-1][c1-2] formula but i tweaked it to correct the extra row and extra column we added during our prefix sum creation by adding 1 to all the indexes
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
