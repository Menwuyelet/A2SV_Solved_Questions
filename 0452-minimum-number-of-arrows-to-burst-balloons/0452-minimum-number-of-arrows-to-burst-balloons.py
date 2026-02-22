class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = len(points)

        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            if prev[1] >= curr[0]:
                ans -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr
            
            
        return ans