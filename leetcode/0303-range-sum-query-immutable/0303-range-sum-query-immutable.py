class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = [0]
        self.nums.extend(nums)

        for i in range(1, len(self.nums)):
            # we start with 2 because we made offset by adding 0 to the bigining of the prefix sum array
            self.nums[i] = self.nums[i - 1] + self.nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        # due to the offset we introduced we add 1 to the right ptr to get the right index, and leave the left as it is.
        return self.nums[right+1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)