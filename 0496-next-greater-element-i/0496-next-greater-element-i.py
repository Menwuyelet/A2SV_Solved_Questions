"""
- The question: we are given two lists of an integer list1 and list2. and we are tasked to construct a list of numbers that tells for every number in list2 that are also in list1 the first number in list2 that is greater than the current one.
- Solution:
    - we first biuld the dictinary containing the next imidiet greter number than the current for list2.
    - after that we iterate through list1 and use the elements in list1 as key to find the next greater number for that number in list two.
    - to construct the dictinary we could use monotonically deacreasing stack.
    - when we find a number that is greater than the number on the top or our stack we pop that number and use it as key to store the larger number that is the next greater number for the number on the top of the stack.
    - after we finish the all numbers on list2 and if ther are numbers on the stack we set their next greater element to -1 as ther is none.
    - after that we construct the answear list using the list1 elements as key.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        stack = []

        # we construct the dictinary using the monotonically decreasing stack
        for num in nums2:
            while stack and stack[-1] < num:
                count[stack[-1]] = num
                stack.pop()
            stack.append(num)

        # we set the next greater number -1 for numbers that didnt have one
        for num in stack:
                count[num] = -1

        # we construct our ans array from the dictinary.  
        ans = []
        for num in nums1:
            ans.append(count[num])
        return ans