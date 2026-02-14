
class Solution(object):
    def findRotation(self, mat, target):
        len_mat = len(mat)
        len_row= len(mat[0])

        for _ in range(4):

            for i in range(len_mat):
                for j in range(i, len_row):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in mat:
                row.reverse()

            if mat == target:
                return True

        return False