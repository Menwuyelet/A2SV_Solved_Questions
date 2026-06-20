class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict()

        for idx in range(len(nums)):
            if nums[idx] in diff:
                return [diff[nums[idx]], idx]
            
            diff[target - nums[idx]] = idx