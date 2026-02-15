class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                min_row = max(i-1, 0)
                max_row = min(i+1, n-1)
                min_column = max(j-1, 0)
                max_column = min(j+1, m-1)
                total = 0
                count = 0
                for r in range(min_row, max_row+1):
                    for c in range(min_column, max_column+1):
                        total += img[r][c]
                        count += 1
                ans[i][j] = total//count

        return ans