"""
- The question: given a list of binary integers we are tasked to delete one integer from it and return the longest sub segment that only contains the integer 1.
- Solution:
    - this is fairly simple sliding window problem.
    - we start with two pointers left and right and move our right until we hit 0 more than twice.
    - when get two zeros we get in to while loop and we move the left pointer towards the right one until we reach it or we pop one zer and we back on only one zero in our segment.
    - after each of the outer loop we update our ans to right - left. we dont add 1 because we are tasked to remove one element from it.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        ans = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            ans = max(ans, right - left)
        
        return ans