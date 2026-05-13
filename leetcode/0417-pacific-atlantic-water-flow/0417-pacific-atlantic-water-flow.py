class Solution:
    def pacificAtlantic(self, heights):
        rows, cols= len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visit):
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visit)

        # Pacific borders
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic borders
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # Intersection
        res = []

        for r in range(rows):

            for c in range(cols):
                
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res