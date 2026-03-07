"""
- The question: given a list of numbers we are tasked to find the runing sum of the list and return each of the runing sum at each level as list.
- Solution:
    - this is fairly easy and straight forward problem,
    - we just need to know about one thing called prefix sum.
    - we just start from the 2nd element and we replace each element with the sum of nums[i-1] + nums[i]
    - then we return the nums.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(1), 
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            # replace nums[i] with nums[i-1] + nums[i]
            nums[i] = nums[i-1] + nums[i]

        return nums

