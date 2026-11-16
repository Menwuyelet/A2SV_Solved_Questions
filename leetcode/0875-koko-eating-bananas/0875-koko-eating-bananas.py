"""
- The question: we are given a list of piles and we are thasked to find the minimum ammount we need to consume at a time to finish the entire piles.
- Solution:
    - this is an optimization problem asking us to mimize the ammount of a consumption at a time.
    - we can consume in range of 1 to infinity, but since we need to mnimize that we define the range to be 1 - max(piles)
    - after that we perform a binary search over the list of possible answers and we take the minimum consuption rate that satisfies the time limit.
- Time and Space complexity:
    - Time = O(n log m), n = len(piles), m = max(piles)
    - space = O(1), 
"""

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

            
