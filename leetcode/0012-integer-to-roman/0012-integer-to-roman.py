"""
- The question: given an integer we are tasked to conver it to roman literals.
- Solution:
    - we can solve this problem using greedy approach.
    - we nested loop one for iteration of the translation values and the second to continuously decrement the num by the current value and assign the appropriate letter to our ans.
-  Time and Space complexity:
    - Time = O(1), since the number is bounded and roman literals will not grow out of "M"
    - space = O(1)
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        ans = []

        for value, leter in values:
            while num >= value:
                ans.append(leter)
                num -= value
        
        return "".join(ans)