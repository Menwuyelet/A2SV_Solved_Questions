"""
- The question: given a matrix(2d list), we are tasked to list all the elements in spiral order.
- Solution:
    - since the constrains are small we can solve this by iterating each cell.
    - to go in the spiral style we need to shring our boundary in each iteration.
    - to track the boundary we can use for boundary variables top, righ, bottom and left.
    - after that we shrink our boundary each time we complete a cycle by updatting these four variables.
-  Time and Space complexity:
    - Time = O(n * m), n = len(row), len(column)
    - space = O(n * m)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            
            # traverse left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # traverse top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # traverse right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # traverse bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
