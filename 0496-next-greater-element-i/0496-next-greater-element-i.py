class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                count[stack[-1]] = num
                stack.pop()
            stack.append(num)


        for num in stack:
                count[num] = -1
            
        ans = []
        for num in nums1:
            ans.append(count[num])
        return ans