"""
- The question: we are given a list of temperatures and tasked to return a list mapping the ammoun of days we need to wait until we find warmer day than the current day.
- Solution:
    - we can solve this problem using monotonicaly decreasing stack.
    - we iterate through the temperatures and we check if the current temp is greater than the temp at the top of the stack,
    - if so we pop it and asign (the index of current temp - the index of the temp at the top) to our ans list.
    - else if it is smaller we append it ot our stack and keep moving.
    - after finishing if there are elements in the stack we map 0 to theire ans list to tell that there are no larger temp days after that day.
-  Time and Space complexity:
    - Time = O(n), n = len(temperatures)
    - space = O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for idx, temp in enumerate(temperatures):
            # we check if the current temperature is warmer than the temperature at the top of the stack.
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = idx - prev

            stack.append(idx)

        return ans