class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [0]
        min_value = float('inf')
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
            min_value = min(min_value, prefix_sum[-1])
        
        if min_value >= 0:
            return 1
        
        return abs(min_value) + 1
        
    
