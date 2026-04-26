"""
- The question: we are given a grid representing a water and an island on it and we are tasked to return the parameter of the island.
- Solution:
    - this is a graph dfs problem.
    - we can solve it using dfs to iterate over all the valid cells and add their parameter to our ans.
    - we start with the first valid land as dfs starting position and we do dfs on it and check if it have a side that is facing water or out of bound if so we add 1 to our ans. 
    - if its sides are land we go to each one by one and check the same thing and do dfs on theire neighbours as well.
    - and that is it.
-  Time and Space complexity:
    - Time = O(n * m), n = len(grid) m = len(grid[0])
    - space = O(n * m), 
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # we initiate visited grid to avoid revisiting cells
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        # we use this list to travel the grid
        direction = [(0,-1), (0,1), (-1, 0), (1, 0)]

        # this is a func we use to check if the next cell is inbound or not
        def inbound(row, col):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
        

        self.ans = 0

        def dfs(row, col):
            visited[row][col] = True
        
            # we iterate over the four directions
            for i, j in direction:

                # we check if a cell is out of bound or water if so we add 1 to our ans
                if not inbound(row+i, col+j) or grid[row+i][col+j] != 1:
                    self.ans += 1

                # else we do dfs for that cell
                elif not visited[row+i][col+j]:
                    dfs(row+i, col+j)

            return
        
   
        # we iterate over the grid to find a starting land
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # when we find a starting grid we call the dfs and return its result and done.
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.ans
        
        # if all the grid is water we return 0 
        return 0
