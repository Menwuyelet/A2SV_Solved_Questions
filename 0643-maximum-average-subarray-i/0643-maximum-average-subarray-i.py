class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left_ptr = 0
        right_ptr = k
        curr_sum = sum(nums[:k])
        max_avg = curr_sum/k

        while right_ptr < len(nums):
            curr_sum -= nums[left_ptr]
            curr_sum += nums[right_ptr]
            max_avg = max((curr_sum/k) , max_avg)

            right_ptr += 1
            left_ptr += 1
        
        return max_avg