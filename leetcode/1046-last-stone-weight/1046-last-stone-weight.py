class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)

        while len(stones) > 1:
            first = heappop_max(stones)
            second = heappop_max(stones)

            if first == second:
                continue
            else:
                heappush_max(stones, first-second)
            
        if stones:
            return stones[0]
        
        return 0