"""
- The question: we are given a list of numbers and tasked to implement a NumArray class that performs a range sum within o(1) time.
- Solution:
    - to do this we could just biuld the prefix sum of the given list and use that to obtain range sum with just one opration.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class NumArray:

    def __init__(self, nums: List[int]):
        # initiate a prefix sum array with 0 as the first element and extending it with the given array
        self.nums = [0]
        self.nums.extend(nums)

        # biulds the prefix sum so we can get the range sum in o(1) by just doing one opration.
        for i in range(2, len(self.nums)):
            # we start with 2 because we made offset by adding 0 to the bigining of the prefix sum array
            self.nums[i] = self.nums[i - 1] + self.nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        # due to the offset we introduced we add 1 to the right ptr to get the right index, and leave the left as it is.
        return self.nums[right+1] - self.nums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)