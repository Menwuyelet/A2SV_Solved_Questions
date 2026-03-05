"""
- The question: we are given a list of integers and we are tasked to find the subsegment with the largest sum and return its sum.
- Solution:
    - to solve this problem we realy just iterate through the number and keep track of curr sum and ans. 
    - every time we get new integer we add it to our curr and check it againist our ans if it would be the max.
    - and we also check if the curr sum is below 0, if so we set the curr sum to 0 to cut out the segment that is produsing negative sum.
    - after finishing we return the ans.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(1), 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            ans = max(ans, curr)

            # checks if we need to cut of the segment before the current integer
            if curr < 0:
                curr = 0

        return ans
