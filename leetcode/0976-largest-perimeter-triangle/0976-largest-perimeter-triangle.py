"""
- The question: given a list of integers, we are tasked to return the maximum perimeter of a triangle that can be formed using 3 nums form the list and the triangle should have area of greater than 0.
- Solution:
    - to do that we sort the nums to make close numbers in one group as much as possible and to make the formation of valid triangle.
    - after sorting we can iterate through the list and check if the three consiquetive numbers form valid triangle and if they do we compare theire perimeter with the current max and take the maximum.
    - to avoid all that we could just start at the back of the sorted list and we can return the first valid triplet since that would be the maximum.
    

-  Time and Space complexity:
    - Time => O(n log n) due to sorting the list
    - space = O(n log n), we only use a constant amount of space to store integers but the sorting alg takes n log n time
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        for right in range(len(nums)-1, 1, -1):

            # we first check if the three consequetive numbers form a valid triangle and since we are starting from the back we can return the first triplet
            if nums[right-2] + nums[right-1] > nums[right]:
                return nums[right - 2] + nums[right - 1] + nums[right]
          
        return 0
                