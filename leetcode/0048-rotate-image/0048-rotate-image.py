"""
- The question: given a matrix(2d list), we are tasked to rotat the cells by 90 degrees.
- Solution:
    - since the constrains are small we can solve this by iterating each cell.
    - to rotate the cell by 90 degrees we need to perform two things.
       1, swap it with its counter part(if cell is located at [i,j], we swap it with [j,i]),
       2, after we swap all the cells once, we reverse each row.
    - the reason we reverse it is because the swaping gives up the transpose of the matrix. by reversing it we finde our rotated matrix.
-  Time and Space complexity:
    - Time = O(n * n), n = len(row), and len(column), but since n <= 20 we can say O(400) = O(1)
    - space = O(n * n), but since n <= 20 we can say O(400) = O(1)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # construct the transpose matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix [j][i] = matrix[j][i], matrix[i][j]

        # reverses each row to make the transpose matrix our rotated image
        for i in range(n):
            matrix[i].reverse()