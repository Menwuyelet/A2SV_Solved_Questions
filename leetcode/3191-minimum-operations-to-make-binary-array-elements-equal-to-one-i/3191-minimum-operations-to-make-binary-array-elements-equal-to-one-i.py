class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left = 0
        count = 0
        if len(nums) == 3 and 0 in nums and 1 in nums:
            return -1

        for right in range(2, len(nums)):
            if nums[left] == 0:
                for i in range(left, left + 3):
                    if nums[i] == 0:
                        nums[i] = 1
                    else:
                        nums[i] = 0

                count += 1
            left += 1
        
        if 0 in nums[left:]:
            
            return -1
        
        return count
