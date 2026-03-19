"""
- The question: we are given a list of poles(wals) represented by theire height, we are tasked to find the tanker that is made by two of the wals.
- Solution:
    - the brute force solution would be to iterate over all the numbers(wals) and compute the area they generate with each of the other numbers and take the maximum.
    - but to do that it will take O(n^2), we can solve the problem using O(n) solution.
    - the solution is simple we use two pointers(coliding) and calculate the area for the two walls and move the pointer with the smalest height.
    - then we take the maiximum as our answer.
-  Time and Space complexity:
    - Time = O(n), n = len(height)
    - space = O(1), 
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1

        highest = 0

        while left_ptr < right_ptr:
            # we take the min because we are bound to its height.
            current_height = min(height[left_ptr], height[right_ptr])
            width = right_ptr - left_ptr

            current_area = current_height * width
            highest = max(highest, current_area)
            
            # we move the pointer that holds the minimum height
            if current_height == height[left_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        
        return highest