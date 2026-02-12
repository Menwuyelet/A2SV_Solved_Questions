"""
- The question: given a matrix (2d list), we are tasked to convert all the rows and columns of 0 appearing cell.
- Solution:
    - since the constraints allow it we solve this by using nested loop multipl times.
    - first we iterate through the matrix and collect the row and column of 0 appearing cell.
    - then we iterate for the row first and set all the row that 0 appears to 0.
    - then we iterate for the column and set all values from multiple rows in that column to 0.
    - we do that in place.
-  Time and Space complexity:
    - Time = O(n * m), n = len(row), len(column)
    - space = O(n+m)
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zeros = set()
        column_zeros = set()

        # this iterates through the matrix and collect all the indexs for 0 containing cell
        for row_idx, row in enumerate(matrix):
            for column_idx, value in enumerate(row):
                if value == 0:
                    row_zeros.add(row_idx)
                    column_zeros.add(column_idx)

        # this iterates through the row_zeros and set all the rows containing 0 to 0
        for row in row_zeros:
            for column in range(len(matrix[row])):
                matrix[row][column] = 0

        # this iterates through the coulumn_zeros and set all the cells in multiple rows in the same colum as the colum containing 0 to 0
        for column in column_zeros:
            for row in matrix:
                row[column] = 0
