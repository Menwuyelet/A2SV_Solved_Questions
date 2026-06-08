class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        size = len(nums)
        if(size < 2):
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, size):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return max(dp[size - 1], dp[size - 2])
