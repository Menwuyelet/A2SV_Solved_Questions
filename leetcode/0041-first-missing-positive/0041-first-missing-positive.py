"""
- The question: we are given a list of integers and tasked to return the first positive number that is not in the list.
- Solution:
    - this problem is easy if the algorithm was not required to be O(n) time and O(1) space.
    - we could use set to add all the numbers in the list and iterate over the posible input size to find the first number that is not in the list, or sort it and check sequetialy.
    - but since we need an algorithm that run in O(n) time and O(1) space it makes the problem hard.
    - to solve it we could use cyclic sorting algorithm and sort the list making all the values sit in there correct index and after that iterate over the list and check if any index is not properly assigned.
    - that will be our missing positive.
- Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # first we sort them using cyclic sort in O(n) time and O(1) space
        n = len(nums)
        for i in range(n):
            while ( 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]):
                    correct_idx = nums[i] - 1
                    nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # then we iterate over the sorted list and check if one of the numbers are missing 
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # if the missing number is outside of the lists range we return the range of the list + 1
        return n + 1

            