class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = defaultdict(int)
        ans = 0
        count[0] = 1

        for num in nums:
            prefix += num
            mod = prefix % k
            ans += count[mod]

            count[mod] += 1

        return ans
    
