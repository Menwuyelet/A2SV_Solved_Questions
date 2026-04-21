"""
- The question: we are given a list of integers and a number and tasked to retur the first index that the number appears in our list and the last element, else if it is not there return -1, -1
- Solution:
    - this is a searching problem and we can use binary search to solve it.
    - but instead of writing the binary search we can use bisect_left and bisect_right functions.
    - to find the first appearance we check bisect left and if number in that indx is equal to our number we check for bisect right to find the last.
    - else if the first element is out of the list range or the number in that indx is not our number we return -1, -1
    - additionaly if the list is empty we return -1, -1
- Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # we handle the empty list case 
        if not nums:
            return [-1, -1]

        left_idx = bisect_left(nums, target)

        # check if our left idx is valid one by checking it possision and its value
        if left_idx >= len(nums) or nums[left_idx] != target:
            return [-1, -1]

        right_idx = bisect_right(nums, target)
        
        return [left_idx, right_idx-1]
