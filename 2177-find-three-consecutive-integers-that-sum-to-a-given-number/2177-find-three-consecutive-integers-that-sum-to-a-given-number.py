"""
- The question: given an integer we are tasked to finde three consecutive integers that are sumed to give that integer.
- Solution:
    - to solve this problem, we can use the fact that the number divisible by 3 is also a sum of the quotient, the quotient-1 and the quotient+1 so we return them.
    - if it is not divisible by 3 then we return [] as there are no such three digits.
-  Time and Space complexity:
    - Time = O(1)
    - space = O(1)
"""

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            return[(num//3)-1, num//3, (num//3)+1]
        return []