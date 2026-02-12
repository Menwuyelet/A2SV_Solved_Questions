"""
- The question: give a number we are tasked to findout if a number is happy or not. a number is said happy if some iteratin of taking its digits and squaring them and adding them it leads to 1. esle if it cant it is unhappy
- Solution:
    - this is cycle detection problem.
    - what we really need to do is keep performing the opration until we find 1 or we find previously seen number.
    - if we find 1 it is happy we can stop, if we see repeated number we are in cycle and we cant reach 1 so stop.
-  Time and Space complexity:
    - Time = O(lon n)
    - space = O(1)
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squared_digits(n)
        return True
    
def sum_of_squared_digits(n):
    digits = str(n)
    sum_ = 0
    for digit in digits:
        sum_ += pow(int(digit), 2)

    return sum_