"""
- The question: we are given a list of integers and an integer limit. we are tasked to find the longest continuous subarray that all the diffrence of its elements are lessthan or equal to the limit.
- Solution:
    - we are asked to return a lengthe of the longest subarray that all its elements diffrense is no more than the limit.
    - we do not need to check all the diffrences of the elements, we can just take the maximum element and minimum element of the subarray and check theire diffrences.
    - if the diffrnece is lower or equal to the limit we increase our subarray length by 1 else we decrease the window form left by 1.
    - we repeat this until we reach the end of the given list.
    - the problem with this approach is we need to check the max and min of each subarray we find to check and that is time costy.
    - so to avoid checking everytime the min and max we can biuld monotonic qeue.
    - we need two qeues one for maximum value and one for minimum value.
    - after we biuld the qeues we check theire top elements diffrence to ditermine the limit is respected.
    - if not we pop from the qeue with the left most element.
    - else we continue to add the next element and check again for the condition and we repeat.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mono_dq_decreasing = deque()
        mono_dq_increasing = deque()
        ans = 0
        left = 0

        for i in range(len(nums)):
            
            # biulde the mono-decreasing qeue to store the next greater element.
            while mono_dq_decreasing and nums[mono_dq_decreasing[-1]] < nums[i]:
                mono_dq_decreasing.pop()
            mono_dq_decreasing.append(i)

            # biulde the mono-increasing qeue to store the next smallest element.
            while mono_dq_increasing and nums[mono_dq_increasing[-1]] > nums[i]:
                mono_dq_increasing.pop()
            mono_dq_increasing.append(i)

            # we check the validity of the condition and we pop from the right qeue to move our window to right,
            while mono_dq_decreasing and mono_dq_increasing and nums[mono_dq_decreasing[0]] - nums[mono_dq_increasing[0]] > limit:
                
                # if the increasing qeue have the left most element we pop from it
                if mono_dq_increasing[0] == left:
                    mono_dq_increasing.popleft()
                
                # if the decreasing qeue have the left most element we pop from it
                if mono_dq_decreasing[0] == left:
                    mono_dq_decreasing.popleft()
                
                # we use left and i to calculate the window size (length of the subarray)
                left += 1

            ans = max(ans, i - left + 1)
            
        return ans
            
            