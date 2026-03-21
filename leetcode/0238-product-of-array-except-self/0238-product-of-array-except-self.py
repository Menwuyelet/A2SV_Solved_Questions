class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodPre= [nums[0]]
        prodPost = [1] * len(nums)
        prodPost[-1] = nums[-1]

        for i in range(1, len(nums)):
            prodPre.append(prodPre[i-1] * nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            prodPost[i] = (prodPost[i+1] * nums[i])
            
        ans = [1]*len(nums)
        for i in range(1, len(nums) - 1):
            ans[i] = prodPre[i-1]*prodPost[i+1]
            
        ans[0] = prodPost[1]
        ans[-1] = prodPre[-2]
    
        return ans
