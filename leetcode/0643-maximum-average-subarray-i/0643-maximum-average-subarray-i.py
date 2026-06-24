class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        ans = curr
        left = 0
        right = k
        while right < len(nums):
            curr -= nums[left]
            curr += nums[right]

            left += 1
            right += 1

            ans = max(ans, curr)
        
        return ans/k