class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_pile = max(piles)
        left = 1
        right = max_pile
        ans = max_pile
        while left <= right:
            mid = (left + right) // 2

            curr = 0
            for i in piles:
                curr += math.ceil(i/mid)
            
            if curr > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans

            
