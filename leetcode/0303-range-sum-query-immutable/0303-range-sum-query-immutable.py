class NumArray:

    def __init__(self, nums: list[int]):
        self.arry = [0]
        # [0,-2,  0, 3, -5,  2,-1]
        self.arry.extend(nums)

        for i in range(1, len(self.arry)):
            self.arry[i] = self.arry[i-1] + self.arry[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.arry[right+1] - self.arry[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)