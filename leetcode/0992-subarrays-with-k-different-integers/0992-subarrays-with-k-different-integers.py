class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return atMostK(nums, k) - atMostK(nums, k - 1)

def atMostK(nums, k):
    count = {}
    left = 0
    res = 0

    for right in range(len(nums)):
        if nums[right] not in count:
            count[nums[right]] = 0
        count[nums[right]] += 1

        # shrink window if too many distinct
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        # count subarrays ending at right
        res += right - left + 1

    return res