"""
- The question: given the horizontal area of ballons, we are tasked to count the minimum number of arrows needed to pop all. 
- Solution:
    - the problem is finding overlaping sub lists.
    - if we find overlaping sub lists that means we can use 1 arrow to pop them.
    - we can have multiple overlaping ballons but we only take the valid one meaning for example:
            - [1,10], [2,5] and [6,7], both the second and thrid lists overlap with the first one but they do not overlap with each other. so we still need two arrows.
            - for [1,10], [2,5] and [4,6] we need one since all are overlaping to each other.
    - we need to sort the points to find the overlaping points.
-  Time and Space complexity:
    - Time = O(n log n), O(n) n = len(points)
    - space = O(n),
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = len(points)

        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]

            if prev[1] >= curr[0]:
                ans -= 1
                # we take the overlaping area as comparation for the next points
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr
            
        return ans
