class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0

        count = defaultdict(int)
        count[0] = 1

        ans = 0

        for num in nums:
            prefix_sum += num

            diff = prefix_sum - goal
            ans += count[diff]

            count[prefix_sum] += 1 
        
        return ans
