class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        right_even = sum(nums[::2])
        right_odd = sum(nums[1::2])

        left_even = left_odd = 0
        ans = 0

        for i, num in enumerate(nums):

            if i % 2 == 0:
                right_even -= num
            else:
                right_odd -= num

            new_even = left_even + right_odd
            new_odd = left_odd + right_even

            if new_even == new_odd:
                ans += 1

            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num

        return ans