class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pr = 0

        for se in range(1,len(nums)):
            if nums[pr] == 0 and nums[se]:
                nums[pr], nums[se] = nums[se], nums[pr]
                pr +=1
            elif nums[pr] != 0:
                pr +=1
            