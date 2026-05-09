"""
- The question: we are given a list containing the heights of the buildings and we are given bricks and laders to climbe the buildings,
                - we use bricks or laders if the next building is taller than the current else we dont need to use one. and we are tasked to return the furthst we can go if we use the bricks and laders optimally
- Solution:
    - so the core idea is that we should use laders for the largest climbes or when we ran out of bricks. 
    - that way we can guarantee optimality.
    - to implement that we use min heap and start with all the climbs as using laders and as we go we check if the current climb is biggest so far we see or we are out of bricks if so we use laders else bricks.
    - we stop when we are out of bricks that means we already used all the laders and bricks and the curren building is the furthest we can go.
-  Time and Space complexity:
    - Time = O(n log n), n = len(stones)
    - space = 1, 
"""

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
            heap = []

            # we iterate untile the last element
            for i in range(len(heights) - 1):
                climb = heights[i + 1] - heights[i]

                # if our climb requires lader or bricks we chose one optimally else we just move to the next
                if climb > 0:
                    heappush(heap, climb)

                    # if the current heap length is larger than the ladders we have we use bricks
                    if len(heap) > ladders:
                        bricks -= heappop(heap)

                    # when we ran out of bricks we stop as we reached our limits.
                    if bricks < 0:
                        return i

            return len(heights) - 1