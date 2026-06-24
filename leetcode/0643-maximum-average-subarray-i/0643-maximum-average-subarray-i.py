class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        initial = sum(nums[:k])
        max_sum = initial

        left, right = 0, k

        while right < len(nums):
            initial += nums[right]
            initial -= nums[left]
            
            max_sum = max(max_sum, initial)

            left += 1
            right += 1
        
        return max_sum/k