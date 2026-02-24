class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1

        highest = 0

        while left_ptr < right_ptr:
            current_height = min(height[left_ptr], height[right_ptr])
            width = right_ptr - left_ptr

            current_area = current_height * width
            highest = max(highest, current_area)
            
            if current_height == height[left_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        
        return highest