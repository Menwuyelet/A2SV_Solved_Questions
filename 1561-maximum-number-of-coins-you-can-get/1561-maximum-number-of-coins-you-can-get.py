"""
- The question: we are given list of coins and 3 freinds. our task is to give the 2nd freind the highest posible pile of coin. all freinds pick greedy.
- Solution:
    - since we pick greedy we first sort it in reverse order and since we are the second freind we iterate through it jumping 2 steps until 2*n where n = len(piles)//3
-  Time and Space complexity:
    - Time = O(n log n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sort_piles = sorted(piles, reverse=True)
        n = len(piles) // 3
        sum = 0

        for i in range(1, 2*n, 2):
            sum+=sort_piles[i]
            
        return(sum)