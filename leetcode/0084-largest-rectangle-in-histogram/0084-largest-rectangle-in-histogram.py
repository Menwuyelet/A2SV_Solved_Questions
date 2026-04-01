class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            if stack and stack[-1][1] <= height:
                stack.append((idx, height))
            elif not stack:
                stack.append((idx, height))
            else:
                while stack and stack[-1][1] > height:
                    temp = stack.pop()
                    area = (idx - temp[0]) * temp[1]
                    max_area = max(max_area, area)

                stack.append((temp[0], height))

        while stack:
            temp = stack.pop()
            area = (len(heights) - temp[0]) * temp[1]
            max_area = max(max_area, area)
            
        return max_area

            
            

