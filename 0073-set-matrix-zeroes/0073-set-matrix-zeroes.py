class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zeros = set()
        column_zeros = set()

        for row_idx, row in enumerate(matrix):
            for column_idx, value in enumerate(row):
                if value == 0:
                    row_zeros.add(row_idx)
                    column_zeros.add(column_idx)

        for row in row_zeros:
            for column in range(len(matrix[row])):
                matrix[row][column] = 0

        for column in column_zeros:
            for row in matrix:
                row[column] = 0
