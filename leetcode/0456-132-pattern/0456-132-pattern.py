"""
- The question: we are given a list of integers and tasked if there is a 132 pattern.
                - that means there should be i, j and k while i < j < k and nums[i] < nums[k] < nums[j]

- Solution:
    - we could solve this by using the brute force approach with O(n^3), but we can optimize it using stack.
    - more precisly monotonically deacreasing stack to track the possible middle numbers and when we maintain the decreasing order.
    - we start from right and go to left and when we get a number whcich disturb the decreasing order we should pop from our stack to correct it and when we do that we update our third number to be that poped number.
    - after that we compare if the current third is greater than the num we are currently on if so we have successfully found our pattern adn can return True.
    - we do the iteration until we finish or hit the pattern and if we finfish before hiting the pattern we return False.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mon_de = deque()
        third = float('-inf')
        
        # we iterate from the back
        for num in nums[::-1]:
            
            # we check if we found the pattern with the current num by comparing it with our third
            if third > num:
                return True

            # we maintain the decreasing order wile updating our third
            while mon_de and mon_de[-1] < num:
                third = mon_de.pop()

            mon_de.append(num)

        return False
