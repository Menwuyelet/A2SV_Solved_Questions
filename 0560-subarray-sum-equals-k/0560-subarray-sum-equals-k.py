class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        ans = 0

        count = {0:1}

        for num in nums:
            prefix_sum += num
            curr = prefix_sum - k

            if curr in count:
                ans += count[curr]
            
            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        
        return ans
     