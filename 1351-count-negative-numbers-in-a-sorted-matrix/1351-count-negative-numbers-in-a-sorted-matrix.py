class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid[::-1]:
            for num in row[::-1]:
                if num >= 0:
                    break
                count += 1
        return count