"""
- The question: we are given a list of integers and a target number and tasked to check if the target is present in the list or not.
- Solution:
    - so this is just a simple search problem.
    - we can solve this using binary search and check wether the target exists or not.
    - since the input is already sorted we dont need to sort it

- Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            
            mid_idx = (right + left) // 2

            # we check if our midle is the target
            if nums[mid_idx] == target:
                return mid_idx

            # we check if we should check next the numbers above our mid indx or bellow it.
            if nums[mid_idx] > target:
                right = mid_idx - 1
            
            if nums[mid_idx] < target:
                left = mid_idx + 1
        
        return -1