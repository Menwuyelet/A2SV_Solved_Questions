class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans_dict = {}
        stack = []

        for idx, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                ans_dict[(prev_temp, prev_idx)] = idx - prev_idx

            stack.append((temp, idx))
            ans_dict[(temp, idx)] = idx

        # remaining ones have no warmer day
        for temp, idx in stack:
            ans_dict[(temp, idx)] = 0

        ans = []
        for idx, temp in enumerate(temperatures):
            ans.append(ans_dict[(temp, idx)])

        return ans
            