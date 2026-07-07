class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        start = 0
        for end in range(len(nums)):
            if end - start > k:
                visited.remove(nums[start])
                start += 1
            if nums[end] in visited:
                return True
            visited.add(nums[end])
        return False