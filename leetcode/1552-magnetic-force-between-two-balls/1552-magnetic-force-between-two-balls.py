"""
- The question: we are given a list of coordinates and tasked to place m balls on these coordinates but the minimum distance of any ballse placed on the coordinates should be maximized.
- Solution:
    - so we can solve this problem by first sorting the coordinates and iterating and trying to place every possible separation from 1 to the maximum separation.
    - but we can optimize it using a binary sarch to find possible placments and using greedy placment afterwards.

-  Time and Space complexity:
    - Time = O(n log n + n log d), n = number positions, d = max position
    - space = O(1), 
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # sort the basket positions
        position.sort()

        # binary search on answer (minimum distance)
        left = 1
        right = position[-1] - position[0]
        answer = 0

        # binary search loop
        while left <= right:
            mid = (left + right) // 2

            # if our mid works we set it as current ans and try bigger possiblities
            if can_place(mid, position, m):
                answer = mid          
                left = mid + 1

            # else we try smaller posiblities
            else:
                right = mid - 1     

        return answer

def can_place(min_dist, position, m):
    # greedy placement
    count = 1
    last_pos = position[0]

    # we iterate over the placments and try all possible positions for the given separation value and check if the current mid value is valid
    for i in range(1, len(position)):
        if position[i] - last_pos >= min_dist:
            count += 1
            last_pos = position[i]

            if count == m:
                return True

    return False