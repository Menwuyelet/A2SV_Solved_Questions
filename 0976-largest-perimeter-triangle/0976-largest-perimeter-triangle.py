"""
- The question: given a list of integers, we are tasked to return the maximum perimeter of a triangle that can be formed using 3 nums form the list and the triangle should have area of greater than 0.
- Solution:
    - to do that we sort the nums to make close numbers in one group as much as possible and to make the formation of valid triangle.
    - after sorting we can iterate through the list and check if the three consiquetive numbers form valid triangle and if they do we compare theire perimeter with the current max and take the maximum.

-  Time and Space complexity:
    - Time => O(n log n) due to sorting the list
    - space = O(1), we only use a constant amount of space to store integers
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter = 0
        left = 0
        right = 2

        subSum = nums[left] + nums[left+1] + nums[right]

        while right < len(nums):
            if nums[left] + nums[left+1] > nums[right]:
                perimeter = max(perimeter, subSum)

            subSum -= nums[left]
            left +=1
            right +=1
            if right < len(nums):
                subSum += nums[right]
          
        
        return perimeter
                