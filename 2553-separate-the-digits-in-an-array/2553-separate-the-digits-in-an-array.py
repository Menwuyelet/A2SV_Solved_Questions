class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            str_num = list(str(num))
            for num in str_num:
                ans.append(int(num))
        return ans