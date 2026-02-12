"""
- The question: given a matrix (2d list), we are tasked to return the transpose of the matrix.
- Solution:
    - transpose of a matrix is obtaind by making the row of the matrix columns.
    - to do that we can use nested loop that the first run on the individual rows, and the second runs on the entire matrix.
    - that is because when we convert rows to colums, number of column of the matrix becomes the row and vice versa, and that causes the change in num of rows and columns.
-  Time and Space complexity:
    - Time = O(n * m), n = len(row), len(column)
    - space = O(n*m)
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        len_matrix = len(matrix)
        len_row = len(matrix[0])
        transpose_matrix = []

        for j in range(len_row):
            temp_row = []
            for i in range(len_matrix):
                temp_row.append(matrix[i][j])
            transpose_matrix.append(temp_row)
        
        return(transpose_matrix)