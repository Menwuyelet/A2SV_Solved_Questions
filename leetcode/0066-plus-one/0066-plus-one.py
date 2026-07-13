class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        left = -1
        nums = digits.copy()
        while nums[left] <= 9:
            if nums[left] < 9:
                nums[left] += 1
                return nums
            nums[left] = 0
            left -= 1
            if left + len(nums) < 0:
                nums.insert(0,1) 
                break
        return nums
