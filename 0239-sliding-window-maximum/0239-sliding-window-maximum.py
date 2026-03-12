class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_dq = deque()
        ans = []

        for i in range(len(nums)):

            # remove indices outside window
            if mono_dq and mono_dq[0] <= i - k:
                mono_dq.popleft()

            # maintain decreasing order
            while mono_dq and nums[mono_dq[-1]] < nums[i]:
                mono_dq.pop()

            mono_dq.append(i)

            # record result
            if i >= k - 1:
                ans.append(nums[mono_dq[0]])

        return ans
