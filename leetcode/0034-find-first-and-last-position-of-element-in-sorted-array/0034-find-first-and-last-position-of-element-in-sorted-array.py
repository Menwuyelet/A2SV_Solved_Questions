class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left_idx = bisect_left(nums, target)

        if left_idx >= len(nums) or nums[left_idx] != target:
            return [-1, -1]

        right_idx = bisect_right(nums, target)
        return [left_idx, right_idx-1]
