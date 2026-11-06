"""
- The question: we are given an integer n and tasked to determine wether the integer is the power of 4 or not.
- Solution:
    - to determine if a number is a power of 4 the easiest way to do it is by deviding it untile we reach undivideble result.
    - this leads to two scenarios,
            1, we keep going further and we reach 1 or
            2, we reach a number less than 1 and greater than 0
    - if we get the first case that means we devided the number and reached 1 that comfirming it our number is a power of 4
    - else if we get the second case we got a number that is not a power of 4.
    - to implement this we can use recursion to recursivly devide the number until we reach one of the two cases.
-  Time and Space complexity:
    - Time = O(log n), n = the input number 
    - space = O(log n), 
"""


def check(n):
    if n == 1:
        return True
    elif n < 1:
        return False

    return check(n/4)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return check(n)
    

    