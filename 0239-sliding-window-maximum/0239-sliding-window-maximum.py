"""
- The question: given a list of numbers and a window size k, we are tasked to return a list containing maximum numbers for each of the window when we move the window one step at a time.
- Solution:
    - the problem with this type of question is they seems easy enough just to use sliding window and compare the current max with the newly added element.
    - but the thing is what if we removed the current max out of the window when we moved it.
    - now we have to find a new local maximum to compare with. and this can happen for all the windows at worst.
    - so to solve this we could use qeue, specifically monotonically decreasing qeue.
    - we store indexes in that qeue, for each iteration we check to remove the elements outside of the current window from the qeue.
    - additionally we check that the newlly added element maintains the monotonicaly decreasing order.
    - else we start poping from the right until we find an element that is larger than the newlly added element.
    - after we append our new element to our qeue, we check the window size valid, and if so we append the first element on the que to our ans as it is the current max.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
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
