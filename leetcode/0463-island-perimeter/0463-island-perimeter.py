class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        self.direction = [(0,-1), (0,1), (-1, 0), (1, 0)]

        def inbound(row, col):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
        

        self.ans = 0

        def dfs(row, col):
            self.visited[row][col] = True
        
            for i, j in self.direction:
                if not inbound(row+i, col+j) or grid[row+i][col+j] != 1:
                    self.ans += 1
            
                elif inbound(row+i, col+j) and grid[row+i][col+j] == 1 and not self.visited[row+i][col+j]:
                    dfs(row+i, col+j)
            return
        
   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.ans
        
        return self.ans
