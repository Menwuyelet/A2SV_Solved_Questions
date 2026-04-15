"""
- The question: we are given a list of numbers that are sorted and rotated and tasked to find the minimum number.
- Solution:
    - this problem is eassy really we just iterate over it and find the smallest number. 
    - but the catch is that we are tasked to write an algorithm that runs in log n time not in n time.
    - so what we do is we use a binary search.
    - the logic is that since the list is sorted and rotated we will have a pattern and a place that the patern will breack.
    - and the possition that the pattern will break is our answer so that is where we use the binary search to find that point.
-  Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(1), 
"""
[3,4,5,1,2]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # we use binary search to find the number that is the first to break the sorted pattern.
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]