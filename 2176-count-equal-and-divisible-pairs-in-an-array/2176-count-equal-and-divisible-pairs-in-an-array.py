class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hold = 0
        seek = 0
        count = 0
        for hold in range(len(nums) - 1):
            for seek in range(hold+1, len(nums)):
                if nums[hold] == nums[seek] and (hold*seek)%2 == 0:
                    count +=1
                    print(hold, seek)
        return count
