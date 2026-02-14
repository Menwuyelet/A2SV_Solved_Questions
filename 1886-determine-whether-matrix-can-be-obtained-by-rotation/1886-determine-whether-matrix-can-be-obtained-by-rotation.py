"""
- The question: we are given two matrixes and we are tasked if matrix mat can be the same as matrix target after rotating it.
- Solution:
    - since our constraint is small we can do this by checking for every rotation.
    - first we try for 90, then 180, and lastly 270
    - to rotate a matrix we find its transpose and reverse each row.
-  Time and Space complexity:
    - Time = O(n^2), n = len(mat)
    - space = O(1)
"""
class Solution(object):
    def findRotation(self, mat, target):
        len_mat = len(mat)
        len_row= len(mat[0])

        for _ in range(4):

            # transpose the matrix
            for i in range(len_mat):
                for j in range(i, len_row):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
           
            # reverse each rows it to make it rotated
            for row in mat:
                row.reverse()

            if mat == target:
                return True

        return False