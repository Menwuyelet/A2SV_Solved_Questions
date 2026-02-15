class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        diagonal = [[] for _ in range(m+n-1)]
        ans = []
        for i in range(n):
            for j in range(m):
                diagonal[i+j].append(mat[i][j])
                
        for i in range(len(diagonal)):
            if i%2 == 0:
                ans += diagonal[i][::-1]
            else: 
                ans += diagonal[i]
        return(ans)