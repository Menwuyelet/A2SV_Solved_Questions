class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
        minutes = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                for x, y in directions:
                    new_row, new_col = row + x, col + y
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row,new_col))
            minutes += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return minutes - 1 if minutes != 0 else 0