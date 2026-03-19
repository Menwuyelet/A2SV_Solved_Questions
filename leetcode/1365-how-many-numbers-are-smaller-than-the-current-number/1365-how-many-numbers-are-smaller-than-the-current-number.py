class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        sorted_nums = sorted(nums)
        ans = []
        for idx, num in enumerate(sorted_nums):
            if num not in counter:
                counter[num] = idx
            
        for num in nums:
            ans.append(counter[num])

        return ans