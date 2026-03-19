"""
- The question: given a list of numbers we are tasked to separate the digits and append them to a lis and return it.
- Solution:
    - to do this we just need to iterate over the numbers separate them and append them to our ans list.
-  Time and Space complexity:
    - Time = O(n*m), where n = len(nums), m = digits of the number
    - space = O(m + n),
"""

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            str_num = list(str(num))
            for num in str_num:
                ans.append(int(num))
        return ans