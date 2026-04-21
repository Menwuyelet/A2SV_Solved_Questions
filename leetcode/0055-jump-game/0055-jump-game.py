"""
- The question: we are given a list of number representing a maximum jump we can make from that element and tasked to check wether we could reach the end of the list or not.
- Solution:
    - so the first thing that comes to mind is to chose the first number and jump at its limit and do that again and again.
    - but the problem with that is we might encounter a case where the max limit jump may contain 0 but there are still valid places to land.
    - to solve that we use diffrent approach.
    - we keep track of a max jump we can make right now, and every time we iterate we compare it with the current index and if it is larger or equal to the current index,
    - we update our max jump to max of it self and our current value plus the index.
    - and we check that the current max jump is larger or equal to th len(nums) - 1 if so we return true.
    - but in the first place if our index is larger than the current max, that means we can return False since we wont be able to reach the end.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(1), 
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i, val in enumerate(nums):
            
            if i <= max_jump:
                max_jump = max(max_jump, val + i)
            
                if max_jump >= len(nums) - 1:
                    return True
            else:       
                return False