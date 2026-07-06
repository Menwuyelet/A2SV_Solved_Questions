class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for  x, a in enumerate(nums):
            if x and a == nums[x-1]:
                continue
            l = x+1
            r = len(nums)-1
            while l < r:
                curr_sum = nums[x] + nums[l] + nums[r]
                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    return target
        
        return ans
        