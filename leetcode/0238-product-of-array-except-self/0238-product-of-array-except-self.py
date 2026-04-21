"""
- The question: we are given a list of numbers and tasked to return a list of numbers for each number a product of the entire array except the number in that possision.
- Solution:
    - this problem seems easy but the presence of zero makes it complicated.
    - due to that we cant use normal prefix sum to solve it.
    - but we can use post fix and pre fix sum and add the two arrays to find the answer array.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodPre= [nums[0]]
        prodPost = [1] * len(nums)
        prodPost[-1] = nums[-1]

        # biuld prefix
        for i in range(1, len(nums)):
            prodPre.append(prodPre[i-1] * nums[i])
        
        # biuld postfix
        for i in range(len(nums)-2, -1, -1):
            prodPost[i] = (prodPost[i+1] * nums[i])
            
        ans = [1]*len(nums)

        # we multiply the two element by element to find the ans
        for i in range(1, len(nums) - 1):
            ans[i] = prodPre[i-1] * prodPost[i+1]

        # we update the first and last number
        ans[0] = prodPost[1]
        ans[-1] = prodPre[-2]
    
        return ans
