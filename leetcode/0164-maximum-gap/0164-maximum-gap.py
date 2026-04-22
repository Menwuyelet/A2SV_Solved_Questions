class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        radix_sort(nums)

        ans = 0
        for i in range(1,len(nums)):
            ans = max(ans, nums[i] - nums[i-1])
        
        return ans 

def radix_sort(nums):
    exp = 1
    max_val = max(nums)

    while max_val // exp > 0:
        counting_sort(nums, exp)
        exp *= 10

def counting_sort(nums, exp):
    n = len(nums)
    output = [0] * n
    count = [0] * 10

    for num in nums:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (nums[i] // exp) % 10
        output[count[index] - 1] = nums[i]
        count[index] -= 1

    for i in range(n):
        nums[i] = output[i]